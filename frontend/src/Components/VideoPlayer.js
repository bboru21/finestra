import React, { useRef, useEffect, useState } from 'react';


const CUEPOINT_MUTE = 'MUTE';
const CUEPOINT_SEEK = 'SEEK';

class Cuepoint {
  start;
  end;
  action;
  fired = false;

  constructor(start, end, action) {
    this.start = start;
    this.end = end;
    this.action = action;
  }
}

// TODO remove cuepointsProp default value
const VideoPlayer = ({
  videoId,
}) => {

  const videoRef = useRef(null);

  useEffect(() => {
    if (videoRef.current) {
      videoRef.current.pause();
      videoRef.current.removeAttribute('src');
      videoRef.current.load();
    }
  });

  const [cuepoints, setCuepoints] = useState(null);
  useEffect(() => {
    const cuepointsFetch = async () => {
      try {
        const jsonData = await (await fetch(`http://localhost:3001/videos/data/cuepoints/${encodeURIComponent(videoId)}`)).json();
        const rawCuepoints = jsonData.data;

        setCuepoints(rawCuepoints.map(c => new Cuepoint(...c)));
      } catch(error) {
        console.error(error);
        setCuepoints([]);
      }
    }

    cuepointsFetch();
  }, [videoId]);

  const processCuepoints = () => {
    cuepoints.forEach(c => {
      if (videoRef.current.currentTime >= c.start && (c.end < 0 || videoRef.current.currentTime < c.end)) {
        if (c.fired) { return; }
        c.fired = true;
        if (c.action === CUEPOINT_MUTE) {
          videoRef.current.muted = true;
        } else if (c.action === CUEPOINT_SEEK) {
          videoRef.current.currentTime = c.end;
        }
      } else {
        if (!c.fired) { return; }
        c.fired = false;
        if (c.action === CUEPOINT_MUTE) {
          videoRef.current.muted = false;
        }
      }
    });
  }

  const handleTimeUpdate = (event) => {
    processCuepoints();
  }

  return (cuepoints ? (
      <video
        ref={videoRef}
        width='320'
        height='240'
        controls
        autoPlay={false}
        onTimeUpdate={(event) => { handleTimeUpdate(event); }}
      >
        <source src={`http://localhost:3001/videos/${videoId}`} type="video/mp4" />
        Your browser does not support the video tag.
      </video>

  ) : (
    <></>
  ));
};

export default VideoPlayer;