import React, { useRef, useState, useEffect } from 'react';
import './App.css';
import songTimer, {playSong} from './timer';

function App() {
  
  const [currArtist, setCurrArtist] = useState(0);
  const [currSongName, setCurrSongName] = useState(0);
  const [currSongUrl, setCurrSongUrl] = useState(0);
  const [currAlbumArt, setCurrAlbumArt] = useState(0);
  const [loading, setLoading] = useState(true);
  const [isPlaying, setIsPlaying] = useState(false);
  const [buttonMoved, setButtonMoved] = useState(false);

  // Create a ref for the audio element
  const audioRef = useRef(null);

  useEffect(() => {
    fetch('/music')
      .then(res => res.json())
      .then(data => {
        setCurrArtist(data.artist)
        setCurrSongName(data.song_name);
        setCurrSongUrl(data.song_url);
        setCurrAlbumArt(data.album_art);
        setLoading(false);
        console.log(data);
      })
      .catch(error => {
        console.error('Error fetching song:', error);
        setLoading(false);
      });

  }, []);

  const handlePlayClick = () => {
    if (audioRef.current) {
      audioRef.current.play();
      playSong();
      setIsPlaying(true);
      setButtonMoved(true);
    }
  };

  const handleFirstPlay = () => {
      console.log("Song has started playing!");
      // Start whatever you need to do after first playback has started
  };

  return (
    <div className="App">
      <header className="App-header">
        {loading ? (
          <p>Loading...</p>
        ) : (
          <>
            {songTimer()}

            <div id="title"> {currSongName} </div>
            <div id="artist"> {currArtist} </div>

            <img id="albumArt" src={currAlbumArt} />
            
            
              <button               
              className={`play-button ${buttonMoved ? 'moved' : ''}`} 
              onClick={handlePlayClick}>Play Song
              </button>
            <audio  ref={audioRef} 
                    id="musicPlayer" 
                    autoplay 
                    onPlay={handleFirstPlay}>
              <source src={currSongUrl} type="audio/mpeg" />
              Your browser does not support the audio element.
            </audio>
          </>
        )}
      </header>
    </div>
  );
}

export default App;