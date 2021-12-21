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

class App extends React.Component {
   constructor(props) {
       super(props)
       this.state = {
           'users': [],
           'projects': [],
           'notes': [],
       }
   }

   componentDidMount() {
       axios.get('http://127.0.0.1:8000/viewsets/users')
           .then(response => {
               const users = response.data
                   this.setState(
                   {
                       'users': users['results']
                   }
               )
           }).catch(error => console.log(error))

       axios.get('http://127.0.0.1:8000/viewsets/projects')
           .then(response => {
               const projects = response.data
               console.log(projects)
                   this.setState(
                   {
                       'projects': projects['results']
                   }
               )
           }).catch(error => console.log(error))

       axios.get('http://127.0.0.1:8000/viewsets/notes')
           .then(response => {
               const notes = response.data
                   this.setState(
                   {
                       'notes': notes['results']
                   }
               )
           }).catch(error => console.log(error))
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
                        </ul>
                    </nav>
                    <Routes>
                        <Route exact path='/' element={<UserList items={this.state.users} />}  />
                        <Route exact path='/notes' element={<NoteList items={this.state.notes} />} />
                        <Route exact path='/projects' element={<ProjectList items={this.state.projects} />} />
                        <Route exact path="/notes/:id" element={<NoteDetails items={this.state.notes} />} />
                        <Route exact path="/projects/:id" element={<ProjectDetails items={this.state.projects} />} />
                    </Routes>
               </BrowserRouter>
           </div>
       )
   }
}

export default App;