import React, { useState, useEffect } from "react";
import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";

const SteeringAngle = () => {
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
    time: item.Time,
    gps_speed: item["GPS Speed"],
    gps_nsat: item["GPS Nsat"],
    gps_lat_acc: item["GPS LatAcc"],
    gps_lon_acc: item["GPS LonAcc"],
    gps_slope: item["GPS Slope"],
    gps_heading: item["GPS Heading"],
    gps_gyro: item["GPS Gyro"],
    gps_altitude: item["GPS Altitude"],
    gps_latitude: item["GPS Latitude"],
    gps_longitude: item["GPS Longitude"],
    fl_shock: item["FL Shock"],
    fr_shock: item["FR Shock"],
    brake_press_front: item.BrakePressFront,
    brake_press_rear: item.BrakePressRear,
    steer_angle_raw: item["Steering AnglRaw"],
    inline_acc: item.InlineAcc,
    lateral_acc: item.LateralAcc,
    vertical_acc: item.VerticalAcc,
    roll_rate: item.RollRate,
    pitch_rate: item.PitchRate,
    yaw_rate: item.YawRate,
    steer_angle: item.SteeringAngle,
    brake_press_f: item["BRK PRESS F"],
    brake_press_r: item["BRK PRESS R"],
    ecu_throttle: item["ECU THROTTLE"]
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
          <Tooltip />
          <Line dataKey="steer_angle_raw" stroke="#8884d8" dot={false} yAxisId="left" name="Steering Angle Raw" />
          <Line dataKey="steer_angle" stroke="#FF0000" dot={false} yAxisId="left" name="Steering Angle" />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
};

export default SteeringAngle;
  