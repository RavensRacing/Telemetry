import React from 'react';
import './App.css';
import ThrottleSpeedChart from './ThrottleSpeed';
//import SteeringAngle from './SteeringAngle';
import { TelemetryDataProvider } from './DataProvider';
import TractionCircle from './TractionCircle';

function App() {

  return (
        <div className="App">
          <TelemetryDataProvider>
            <ThrottleSpeedChart />
            <TractionCircle />
          </TelemetryDataProvider>
    </div>
  );
}

export default App;
