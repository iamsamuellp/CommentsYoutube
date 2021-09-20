import Search from './Components/Searchbar/searchbar.jsx';
import axios from 'axios';
import React, { Component } from 'react';
//import youtubeAPIKey from './APIKEY';


class App extends Component {
  constructor(props){
    super(props);
    this.state = { 

     }
    }
  
  
  
  
  // handleSubmit = async (searchTerm) => {
  //   try{
  //     let query = "https://www.googleapis.com/youtube/v3/search?q=" + searchTerm +"&key=" + youtubeAPIKey + "&part=snippet&type=video";
  //     const result = await axios.get(query)
  //     this.setState({videoList: result.data.items})
  //   }
  //   catch (ex){
  //     console.log("Can't get video: " + ex)
  //   }
  // }
  render () {
    return (
      <div>
        <h1>Hello World </h1>
      </div>
    );
  } 
}

export default App;


