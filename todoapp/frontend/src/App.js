import React from 'react';
import logo from './logo.svg';
import './App.css';
import UserList from './components/TodoUser.js'
import NoteList from './components/TodoNotes.js'
import NoteDetails from './components/NoteDetails.js'
import ProjectList from './components/Projects.js'
import ProjectDetails from './components/ProjectDetails.js'
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

    componentDidMount() {
        this.get_token_from_storage()
    }


   render () {

    console.log(this.state.username, this.state.token)
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
                        <Route exact path='/' element={<UserList items={this.state.users} />}  />
                        <Route exact path='/notes' element={<NoteList items={this.state.notes} />} />
                        <Route exact path='/projects' element={<ProjectList items={this.state.projects} />} />
                        <Route exact path="/notes/:id" element={<NoteDetails items={this.state.notes} />} />
                        <Route exact path="/projects/:id" element={<ProjectDetails items={this.state.projects} />} />
                        <Route exact path='/login' element={<LoginForm get_token={(username, password) => this.get_token(username, password)} />} />} />
                    </Routes>
               </BrowserRouter>
           </div>
       )
   }

}

export default App;