import Search from './Components/Searchbar/searchbar.jsx';
import axios from 'axios';
import React, { Component, useEffect, useState } from 'react';
//import youtubeAPIKey from './APIKEY';
import EmbedVideo from "./Components/VideoPlayer/VideoPlayer";
import VideoPlayer from './Components/VideoPlayer/VideoPlayer';
import ShowComments from './Components/Comments/ShowComments.jsx';


const App = () => {
  const [comments, setComments] =useState([]);
  const [filteredVideo, filteredVideos] =useState('freerunning 2021')
async function fetchComments() {
  let response = await axios.get(`https://www.youtube.com/watch?v=${filteredVideo}`);
  setComments(response.data.results);
}

function mapComments(){
  console.log("map comments");
  return comments.map(comment =>
    <ShowComments
    key={comment.video_Id}
    comment={comment}
    />
    )
}

useEffect(() => {
  console.log("use effect");
  let mounted = true;
  if(mounted){
    fetchComments();
  }
  return () => mounted = false;
}, [])

    return (
    <VideoPlayer url="https://www.youtube.com/watch?v=l3Kh9X27NF8" />
  );
}
export default App;

