import React, {useContext } from "react";
import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";
import { TelemetryDataContext } from "./DataProvider";

const ThrottleSpeedChart = () => {

    const { data, dataIsLoaded } = useContext(TelemetryDataContext);

  if (!dataIsLoaded) {
    return <p>Loading...</p>;
  }

  console.log(data);

  return (
    <div style={{ width: "100%", height: 300 }}>
      <ResponsiveContainer>
        <LineChart data={data}>
          <XAxis dataKey="time" stroke="white" />
          <YAxis yAxisId="left" orientation="left" stroke="white"/>
          <YAxis yAxisId="right" orientation="right" stroke="white"/>
          <Tooltip />
          <Line dataKey="gps_speed" stroke="#8884d8" dot={false} yAxisId="left" name="GPS Speed" />
          <Line dataKey="ecu_throttle" stroke="#FF0000" dot={false} yAxisId="left" name="Throttle Position" />
          <Line dataKey="brake_press_front" stroke="#00FF00" dot={false} yAxisId="right" name="Brake Pressure" />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
};

export default ThrottleSpeedChart;
  