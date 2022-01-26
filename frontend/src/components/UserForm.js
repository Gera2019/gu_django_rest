import React from 'react'


class UserForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {username: '', firstname: '', lastname:'', email: '', age: 30, password: ''}
    }

    handleChange(event) {
        this.setState({
            [event.target.name]: event.target.value
        });
    }

    handleSubmit(event) {
      this.props.create_user(this.state.username, this.state.firstname, this.state.lastname, this.state.email, this.state.age, this.state.password)
      event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event)=> this.handleSubmit(event)}>
                <div className="form-group">
                    <label for="login">Username</label>
                    <input type="text" className="form-control" name="username" value={this.state.username} onChange={(event)=>this.handleChange(event)} />
                </div>

                <div className="form-group">
                    <label for="firstname">First name</label>
                    <input type="text" className="form-control" name="firstname" value={this.state.firstname} onChange={(event)=>this.handleChange(event)} />
                </div>

                <div className="form-group">
                    <label for="lastname">Last name</label>
                    <input type="text" className="form-control" name="lastname" value={this.state.lastname} onChange={(event)=>this.handleChange(event)} />
                </div>

                <div className="form-group">
                    <label for="email">Email</label>
                    <input type="text" className="form-control" name="email" value={this.state.email} onChange={(event)=>this.handleChange(event)} />
                </div>

                <div className="form-group">
                    <label for="age">Age</label>
                    <input type="number" className="form-control" name="age" value={this.state.age} onChange={(event)=>this.handleChange(event)} />
                </div>

                <div className="form-group">
                    <label for="password">Password</label>
                    <input type="password" className="form-control" name="password" value={this.state.password} onChange={(event)=>this.handleChange(event)} />
                </div>

                <input type="submit" className="btn btn-primary" value="Save" />
            </form>
        );
    }
}

export default UserForm