import React, { Component } from 'react';
import { DynamicBarChart } from 'react-dynamic-charts';
import 'react-dynamic-charts/dist/index.css';

class Dynamicchart extends Component {
  constructor(props) {
    super(props)
    
    this.state = {
      data: [{ "name": "Call", "values": [] }]
      
    }
    
    // this.getDatafromapi=this.getDatafromapi.bind(this)
    // console.log(this.state)
    // this.getDatafromapi()
    // super(props)
    // this.componentWillUpdate()
  }

  
  
  componentDidMount = (event) => {
    const mockData = [
      {
        id: 1,
        value: 10,
        label: "hey",
        color: "red"
      }
    ]
    const newwData = [{
      "name": "Call1",
      "values": mockData
    }]

    this.setState({
      data:newwData
    });
     
    // console.log("next====",this.state.data)
  }
  // getDatafromapi =  () => {
    // const res = await fetch("http://127.0.0.1:5000/getdata")
    // let datas = await res.json();
    // datas = datas.map(x => {
      
    //   return {
    //     id:x.id,
    //     value:x.value,
    //     label:x.label,
    //     color:x.color
    //   }
    // })
    // // console.log(datas)
    
    // this.setState({data : newwData});
    
  //   this.setState({
  //     data:newwData
  //   },()=>console.log("then===",this.state.data));
     
  //   console.log("next====",this.state.data)
  // // return this.state
  // }
// }


  render() {
    // console.log('render====',this.state.data)
    
    return (
      <div>
      <DynamicBarChart
      
        data={this.state.data}

      />
      </div>
    );
  }

}

export default Dynamicchart