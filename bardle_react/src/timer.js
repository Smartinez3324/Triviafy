import React from "react";
import { CountdownCircleTimer } from "react-countdown-circle-timer";

import "./timer.css";

let paused = true;

export function playSong() {
    paused = false;
}

const renderTime = ({ remainingTime }) => {
  if (remainingTime === 0) {
    return <div className="timer"> 0 </div>;
  }

  return (
    <div className="timer">
      <div className="value">{remainingTime}</div>
    </div>
  );
};

function songTimer() {
  return (
      <div className="timer-wrapper">
        <CountdownCircleTimer
          isPlaying={!paused}
          duration={30}
          strokeWidth={15}
          strokeLinecap="square"
          trailColor="#fbf1c7" // Cream Color
          colors={["#d79921", "#d17a08", "#d14808", "#d11208"]}
          colorsTime={[20, 13, 6, 0]}
          onComplete={() => ({ shouldRepeat: false })}
        >
            {renderTime}
          
        </CountdownCircleTimer>
      </div>
  );
};

// Returns HTML for songTimer
export default songTimer;