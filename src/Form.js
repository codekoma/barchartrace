import React from 'react';

export default class Form extends React.Component{
    state={
        algoName:'',
        Status:'',
    };

    change = e =>{
        this.setState({
           [e.target.name]:e.target.value
        });
    };

    onSubmit= e =>{
        e.preventDefault();
        console.log(this.state);
    };
    
    
    render(){
        return(
            <form>
                <label>Algoname:
                    <input 
                    name="AlgoName"
                    placeholder="algoname" 
                    value={this.state.algoName} 
                    onChange={e => this.change(e)}/>
                </label>

               <br />
                
                <label>status:
                    <input 
                    name="Status"
                    
                    value="STOP"
                    //onChange={e => this.change(e)}/>
                    />
                </label>
                
                <br />
                <label>Username:
                    <input 
                    name="userName"
                    placeholder="username" 
                    value={this.state.userName} 
                    onChange={e => this.change(e)}/>

                </label>
               
                <br />
                <label>Email:
                    <input 
                    name="email"
                    placeholder="email" 
                    value={this.state.email} 
                    onChange={e => this.change(e)}/>

                </label>
               
                <br />
                
                <label>Password:
                    <input
                    name="passWord" 
                    placeholder="password" 
                    value={this.state.passWord} 
                    onChange={e => this.change(e)}/>

                </label>
                
                <br />
                <button onClick={ e => this.onSubmit(e) } > Submit </button>

                
            </form>

        );
    }
}


