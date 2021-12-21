import React from 'react'
import { Link } from 'react-router-dom'


const NoteItem = ({item}) => {
   return (
       <tr>
           <td><Link to={`${item.id}`}>{item.id}</Link></td>
           <td>
               {item.userid.username}
           </td>
           <td>
               {item.projectid}
           </td>

           <td>
               {item.created}
           </td>
           <td>
               {item.updated}
           </td>
       </tr>
   )
}

const NoteList = ({items}) => {
   return (
       <table>
           <th>
               ID
           </th>
           <th>
               User
           </th>
           <th>
               Project ID
           </th>

           <th>
               Created
           </th>
           <th>
               Updated
           </th>
           {items.map((item) => <NoteItem item={item} />)}
       </table>
   )
}


export default NoteList