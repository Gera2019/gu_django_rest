import React from 'react'
import { Link } from 'react-router-dom'


const ProjectItem = ({item, delete_project}) => {
   return (
           <tr>
               <td> <Link to={`${item.id}`}>{item.id}</Link> </td>
               <td> {item.name} </td>
               <td> {item.users.join(',')} </td>
               <td>
                    <button onClick={()=>delete_project(item.id)} type='button'>Delete</button>
               </td>
           </tr>
   )
}

const ProjectList = ({items, delete_project}) => {
   return (
        <div>
         <input
                type="text"
                placeholder="Search"
         />
           <table>
               <th> ID </th>
               <th>
                   Name
               </th>
               <th>
                   Users
               </th>
               <th></th>
               {items.map((item) => <ProjectItem item={item} delete_project={delete_project} />)}
           </table>
           <Link to='/projects/create'>Create</Link>
       </div>
   )
}

export default ProjectList