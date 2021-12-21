import React from 'react'
import { useParams } from 'react-router-dom'

const NoteItem = ({item}) => {

    return (
        <table>
            <tr>
                <td>{item.id}</td>
                <td>{item.user}</td>
                <td>{item.text}</td>
            </tr>
        </table>
    )
}

const NoteDetails = ({items}) => {
    let { id } = useParams();
    let filtered_item = items.filter((item) => item.id == id)
    return (
        <table>
            <tr>
                <th>ID</th>
                <th>User</th>
                <th>Text</th>
            </tr>
            {filtered_item.map((item) => <NoteItem item={item} />)}
        </table>
   )
}


export default NoteDetails