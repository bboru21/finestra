import { useState, useEffect } from 'react';
import './App.css';

import VideoPlayer from './Components/VideoPlayer';

function App() {

  const [videoId, setVideoId] = useState(null);
  const [videoFileMap, setVideoFileMap] = useState(null);

  useEffect(() => {
    fetch("http://localhost:3001/videos/data", {
      method: "GET",
    })
      .then((response) => response.json())
      .then((json) => {
        setVideoFileMap(json.data);
      })
  }, []);

  function playVideo(event, videoId) {
    event.preventDefault();
    setVideoId(videoId);
  }
  return (
    <div className="App">
      {videoId && (
        <VideoPlayer
          videoId={videoId}
        >
        </VideoPlayer>
      )} <br />

      <div class="videoList">
      {videoFileMap && Object.keys(videoFileMap).map(k => (
        <div>
          <button
            key={k}
            onClick={(event) => { playVideo(event, k); }}
            className="unstyledButton"
          >
            {k}
          </button>
        </div>
      ))}
      </div>
    </div>
  );
}

export default App;
