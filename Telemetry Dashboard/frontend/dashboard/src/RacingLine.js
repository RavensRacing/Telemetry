import React, {useContext } from "react";
import { Scatter, XAxis, YAxis, Tooltip, ResponsiveContainer, ScatterChart } from "recharts";
import { TelemetryDataContext } from "./DataProvider";

const RacingLine = () => {

    const { data, dataIsLoaded } = useContext(TelemetryDataContext);

  if (!dataIsLoaded) {
    return <p>Loading...</p>;
  }

  console.log(data);

  return (
    <div style={{ width: "100%", height: 1000 }}>
      <ResponsiveContainer>
        <ScatterChart>
          <XAxis type="number" dataKey="gps_longitude" />
          <YAxis type="number" dataKey="gps_latitude" domain={[44.491, 44.495]}/>
          <Tooltip />
          <Scatter data={data} fill="red"/>
        </ScatterChart>
      </ResponsiveContainer>
    </div>
  );
};

export default RacingLine;
  