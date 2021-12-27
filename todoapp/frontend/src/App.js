import React from 'react';
import logo from './logo.svg';
import './App.css';
import UserList from './components/TodoUser.js'
import ProjectList from './components/Projects.js'
import axios from 'axios'

class App extends React.Component {
   constructor(props) {
       super(props)
       this.state = {
           'users': [],
//           'projects': [],
       }
   }

   componentDidMount() {
       axios.get('http://127.0.0.1:8000/api/users')
           .then(response => {
               const users = response.data
                   this.setState(
                   {
                       'users': users
                   }
               )
           }).catch(error => console.log(error))

      axios.get('http://127.0.0.1:8000/api/projects')
           .then(response => {
               const projects = response.data
                   this.setState(
                   {
                       'projects': projects
                   }
               )
           }).catch(error => console.log(error))
    }


   render () {
       return (
           <div>
               <UserList users={this.state.users} />
               <ProjectList projects={this.state.projects} />
           </div>
       )
   }
}

export default App;