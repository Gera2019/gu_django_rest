import React from 'react'
import { Link } from 'react-router-dom'


const NoteItem = ({item, delete_note}) => {
   return (
       <tr>
           <td><Link to={`${item.id}`}>{item.id}</Link></td>
           <td>
               {item.userid.username}
           </td>
           <td>
               {item.projectid.name}
           </td>
           <td>
               {item.created}
           </td>
           <td>
               {item.updated}
           </td>
            <td>
                <button onClick={()=>delete_note(item.id)} type='button'>Delete</button>
            </td>
       </tr>
   )
}

const NoteList = ({items, delete_note}) => {
   return (
        <div>
           <table>
               <th>
                   ID
               </th>
               <th>
                   User
               </th>
               <th>
                   Project Name
               </th>

               <th>
                   Created
               </th>
               <th>
                   Updated
               </th>
               <th></th>
               {items.map((item) => <NoteItem item={item} delete_note={delete_note} />)}
           </table>
           <Link to='/notes/create'>Create</Link>
       </div>
   )
}


export default NoteList