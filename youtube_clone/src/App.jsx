import Searchbar from './searchbar';


class App extends Component {
  constructor(props) {
    super(props);
    this.state = {  }
  }
  render() { 
    
  }
}
handleSubmit = async (searchTerm) => {
  try{
    let query = "https://www.googleapis.com/youtube/v3/search?q=" + searchTerm +"&key=" + youtubeAPIKey + "&part=snippet&type=video";
    const result = await axios.get(query)
    this.setState({videoList: result.data.items})
  }
  catch (ex){
    console.log("error getting video: " + ex)
  }
}
export default App;


