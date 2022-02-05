import React from 'react'
import { useParams } from 'react-router-dom'

const ProjectItem = ({item}) => {
    return (
            <tr>
                <td>{item.name}</td>
                <td>{item.users.join(', ')}</td>
                <td>{item.url}</td>
            </tr>
    )
}

const ProjectDetails = ({items}) => {
    let { id } = useParams();
    let filtered_item = items.filter((item) => item.id == id)
    return (
        <table>
            <tr>
                <th>Name</th>
                <th>Users</th>
                <th>URL</th>
            </tr>
            {filtered_item.map((item) => <ProjectItem item={item} />)}
        </table>
   )
}


export default ProjectDetails