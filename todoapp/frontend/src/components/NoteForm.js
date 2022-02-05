import React from 'react'


class NoteForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {username: '', project: '', text: ''}
    }

    handleChange(event) {
        this.setState({
            [event.target.name]: event.target.value
        });
    }

    handleSubmit(event) {
      this.props.create_note(this.state.username, this.state.project, this.state.text)
      event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event)=> this.handleSubmit(event)}>
                <div className="form-group">
                    <label for="name">Username</label>
                    <select name="username" onChange={(event)=>this.handleChange(event)}>
                        {this.props.users.map((user) => <option value={user.id}>{user.firstName} {user.lastName}</option>)}
                    </select>
                </div>

                <div className="form-group">
                    <label for="project">URL</label>
                    <select name="project" onChange={(event)=>this.handleChange(event)}>
                        {this.props.projects.map((project) => <option value={project.id}>{project.name}</option>)}
                    </select>
                    </div>

                <div className="form-group">
                    <label for="text">Text</label>
                    <input type="text" className="form-control" name="text" value={this.state.text} onChange={(event)=>this.handleChange(event)} />

                </div>

                <input type="submit" className="btn btn-primary" value="Save" />
            </form>
        );
    }
}

export default NoteForm