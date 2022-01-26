import React from 'react';
import logo from './logo.svg';
import './App.css';
import UserList from './components/TodoUser.js'
import NoteList from './components/TodoNotes.js'
import NoteDetails from './components/NoteDetails.js'
import ProjectList from './components/Projects.js'
import ProjectDetails from './components/ProjectDetails.js'
import UserForm from './components/UserForm.js'
import ProjectForm from './components/ProjectForm.js'
import NoteForm from './components/NoteForm.js'
import {HashRouter, BrowserRouter,  Route, Routes, Link, Switch, Navigate} from 'react-router-dom'
import axios from 'axios'
import LoginForm from './components/Auth.js'
import Cookies from 'universal-cookie';


class App extends React.Component {
    constructor(props) {
       super(props)
       this.state = {
           'users': [],
           'projects': [],
           'notes': [],
           'token': '',
           'username':'',
       }
    }
    set_token(token, username) {
        const cookies = new Cookies();
        cookies.set('token', token);
        cookies.set('username', username);
        this.setState({'token': token, 'username': username}, ()=>this.load_data())
    }

    is_authenticated() {
        return this.state.token != ''
    }

    logout() {
        this.set_token('', '')
    }

    get_token_from_storage() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        const username = cookies.get('username')
        this.setState({'token': token, 'username': username}, ()=>this.load_data())
    }

    get_token(username, password) {
        axios.post('http://127.0.0.1:8000/api-token-auth/', {username: username, password: password})
        .then(response => {
            this.set_token(response.data['token'], username)
        }).catch(error => alert('Неверный логин или пароль'))
    }


    get_headers() {
        let headers = {
          'Content-Type': 'application/json'
        }

        if (this.is_authenticated())
            {
                headers['Authorization'] = 'Token ' + this.state.token;
            }
        return headers
    }

    load_data() {
        const headers = this.get_headers()

        axios.get('http://127.0.0.1:8000/viewsets/users', {headers})
           .then(response => {
               this.setState(
                   {
                       'users': response.data['results']
                   }
               )
           }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/viewsets/projects', {headers})
           .then(response => {
                this.setState(
                   {
                       'projects': response.data['results']
                   }
               )
           }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/viewsets/notes', {headers})
           .then(response => {
                this.setState(
                   {
                       'notes': response.data['results']
                   }
               )
           }).catch(error => console.log(error))
    }

    delete_user(id) {
        let headers = this.get_headers()
        axios
        .delete(`http://127.0.0.1:8000/viewsets/users/${id}`, {headers})
        .then(response => {
            const users = response.data['results']
            this.setState({
                'users': this.state.users.filter((item) => item.id != id)
            })
        })
        .catch(error => {
            console.log(error)
        })
    }

    delete_project(id) {
        let headers = this.get_headers()
        axios
        .delete(`http://127.0.0.1:8000/viewsets/projects/${id}`, {headers})
        .then(response => {
            const projects = response.data['results']
            this.setState({
                'projects': this.state.projects.filter((item) => item.id != id)
            })
        })
        .catch(error => {
            console.log(error)
        })
    }

    delete_note(id) {
        let headers = this.get_headers()
        axios
        .delete(`http://127.0.0.1:8000/viewsets/notes/${id}`, {headers})
        .then(response => {
            const notes = response.data['results']
            this.setState({
                'users': this.state.notes.filter((item) => item.id != id)
            })
        })
        .catch(error => {
            console.log(error)
        })
    }

    create_user(username, firstname, lastname, email, age, password) {
        const headers = this.get_headers()
        const data = {
            username: username,
            firstName: firstname,
            lastName: lastname,
            email: email,
            age: age,
            password: password
        }

        axios.post(`http://127.0.0.1:8000/viewsets/users/`, data, {headers})
            .then(response => {
              let new_user = response.data['results']
              this.setState({users: [...this.state.users, new_user]})
            }).catch(error => console.log(error))
    }

    create_project(name, url, users) {
        const headers = this.get_headers()
        const data = {
            name: name,
            url: url,
            users: users,
        }

        axios.post(`http://127.0.0.1:8000/viewsets/projects/`, data, {headers})
            .then(response => {
              let new_project = response.data['results']
              const users = this.state.users.filter((item) => item.id === new_project.user)[0]
              new_project.users = users
              this.setState({projects: [...this.state.projects, new_project]})
            }).catch(error => console.log(error))
    }

    create_note(username, project, text) {
        const headers = this.get_headers()
        const data = {
            userid: username,
            projectid: project,
            text: text,
        }

        axios.post(`http://127.0.0.1:8000/viewsets/notes/`, data, {headers})
            .then(response => {
              let new_note = response.data['results']
              this.setState({notes: [...this.state.notes, new_note]})
            }).catch(error => console.log(error))
    }

    componentDidMount() {
        this.get_token_from_storage()
    }

    render () {
       return (
           <div className="App">
               <BrowserRouter>
                    <nav>
                        <ul>
                            <li>
                                <Link to='/'>Users</Link>
                            </li>
                            <li>
                                <Link to='/notes'>Notes</Link>
                            </li>
                            <li>
                                <Link to='/projects'>Projects</Link>
                            </li>
                            <li>
                                {this.state.username}
                            </li>
                            <li>
                                {this.is_authenticated() ? <button onClick={()=>this.logout()}>Logout</button> : <Link to='/login'>Login</Link>}
                            </li>

                        </ul>
                    </nav>

                    <Routes>
                        <Route exact path='/' element={<UserList items={this.state.users} delete_user={(id) => this.delete_user(id)} />} />
                        <Route exact path='/create' element={<UserForm create_user={(username,firstname,lastname,email,age,password) => this.create_user(username, firstname, lastname, email, age, password)}/>}  />
                        <Route exact path='/notes' element={<NoteList items={this.state.notes} delete_note={(id) => this.delete_note(id)}/>} />
                        <Route exact path='/projects' element={<ProjectList users={this.state.users} items={this.state.projects} delete_project={(id) => this.delete_project(id)}/>} />
                        <Route exact path='/projects/create' element={<ProjectForm users={this.state.users} create_project={(name, url, users) => this.create_project(name, url, users)} />}  />
                        <Route exact path="/notes/:id" element={<NoteDetails items={this.state.notes} />} />
                        <Route exact path='/notes/create' element={<NoteForm users={this.state.users} projects={this.state.projects}  create_note={(username, project, text) => this.create_note(username, project, text)} />}  />
                        <Route exact path="/projects/:id" element={<ProjectDetails items={this.state.projects} />} />
                        <Route exact path='/login' element={<LoginForm get_token={(username, password) => this.get_token(username, password)} />} />} />

                    </Routes>
               </BrowserRouter>
           </div>
       )
   }

}

export default App;