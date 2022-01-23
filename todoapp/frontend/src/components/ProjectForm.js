import React from 'react'


class ProjectForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {name: '', url: '', users: []}
    }

    handleChange(event) {
        this.setState({
            [event.target.name]: event.target.value
        });
    }

    handleUsersChange(event) {
        if (!event.target.selectedOptions) {
            return;
        }

        let users = []
        for (let i=0; i<event.target.selectedOptions.length; i++) {
            users.push(parseInt(event.target.selectedOptions.item(i).value))
        }

        this.setState({
            'users': users
        })
    }


    handleSubmit(event) {
      this.props.create_project(this.state.name, this.state.url, this.state.users)
      event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event)=> this.handleSubmit(event)}>
                <div className="form-group">
                    <label for="name">Name</label>
                    <input type="text" className="form-control" name="name" value={this.state.name} onChange={(event)=>this.handleChange(event)} />
                </div>

                <div className="form-group">
                    <label for="url">URL</label>
                    <input type="text" className="form-control" name="url" value={this.state.url} onChange={(event)=>this.handleChange(event)} />
                </div>

                <div className="form-group">
                    <label for="users">Users</label>
                    <select multiple name="authors" onChange={(event) => this.handleUsersChange(event)}>
                        {this.props.users.map((item) => <option value={item.id}>{item.firstName} {item.lastName}</option>)}
                    </select>
                </div>

                <input type="submit" className="btn btn-primary" value="Save" />
            </form>
        );
    }
}

export default ProjectForm