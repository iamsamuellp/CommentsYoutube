import ReactPlayer from 'react-player/youtube';

const VideoPlayer = (props) => {
  return (
    <ReactPlayer url={props.url} />
  );
}
export default VideoPlayer;
