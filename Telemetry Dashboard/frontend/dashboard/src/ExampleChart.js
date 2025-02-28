import React, { useState, useEffect } from "react";
import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";

const ThrottleSpeedChart = () => {
  const [items, setItems] = useState([]);
  const [dataIsLoaded, setDataIsLoaded] = useState(false);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/telemetry/")
      .then((res) => res.json())
      .then((json) => {
        setItems(json);
        setDataIsLoaded(true);
      })
      .catch((error) => console.error("Error fetching data:", error));
  }, []);


  const data = items.map((item, index) => ({
    time: item.Time, // Modify this to match your API data field
    gps_speed: item["GPS Speed"], // Replace with the correct field from API
    throttle_pos: item["ECU THROTTLE"]
  }));

  if (!dataIsLoaded) {
    return <p>Loading...</p>;
  }

  return (
    <div style={{ width: "100%", height: 300 }}>
      <ResponsiveContainer>
        <LineChart data={data}>
          <XAxis dataKey="time" stroke="white" />
          <YAxis yAxisId="left" orientation="left" stroke="white"/>
          <YAxis yAxisId="right" orientation="right" stroke="white"/>
          <Tooltip />
          <Line dataKey="gps_speed" stroke="#8884d8" dot={false} yAxisId="left" name="GPS Speed" />
          <Line dataKey="throttle_pos" stroke="#FF0000" dot={false} yAxisId="right" name="Throttle Position" />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
};

export default ThrottleSpeedChart;
  