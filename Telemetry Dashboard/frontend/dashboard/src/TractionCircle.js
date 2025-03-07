import React, {useContext } from "react";
import { Scatter, XAxis, YAxis, Tooltip, ResponsiveContainer, ScatterChart } from "recharts";
import { TelemetryDataContext } from "./DataProvider";

const TractionCircle = () => {

    const { data, dataIsLoaded } = useContext(TelemetryDataContext);


  if (!dataIsLoaded) {
    return <p>Loading...</p>;
  }

  return (
    <div style={{ width: "50%", height: 500 }}>
      <ResponsiveContainer>
        <ScatterChart data={data}>
          <XAxis dataKey="gps_lat_acc" />
          <YAxis dataKey="gps_lon_acc" />
          <Tooltip />
          <Scatter data={data} fill="green"/>
        </ScatterChart>
      </ResponsiveContainer>
    </div>
  );
};

export default TractionCircle;
  