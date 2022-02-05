import React from 'react'
import {Link} from 'react-router-dom'


const UserItem = ({item, delete_user}) => {
   return (
       <tr>
           <td>
               {item.username}
           </td>
           <td>
               {item.firstName}
           </td>
           <td>
               {item.lastName}
           </td>
           <td>
               {item.email}
           </td>
           <td>
                <button onClick={()=>delete_user(item.id)} type='button'>Delete</button>
           </td>
       </tr>
   )
}

const UserList = ({items, delete_user}) => {

   return (
        <div>
           <table>
               <th>
                   Username
               </th>
               <th>
                   First name
               </th>
               <th>
                   Last Name
               </th>
               <th>
                   Email
               </th>
               <th></th>
               {items.map((item) => <UserItem item={item} delete_user={delete_user} />)}
           </table>
            <Link to='/create'>Create</Link>
       </div>
   )
}


export default UserList