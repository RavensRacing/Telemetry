import React from 'react';
import './App.css';
import ThrottleSpeedChart from './ThrottleSpeed';
import TractionCircle from './TractionCircle';
import { TelemetryDataProvider } from './DataProvider';
import RacingLine from './RacingLine';

function App() {

  return (
        <div className="App">
          <TelemetryDataProvider>
            <ThrottleSpeedChart />
            <div>
              <TractionCircle />
              <RacingLine />
            </div>

          </TelemetryDataProvider>
    </div>
  );
}

export default App;
