import React, { createContext, useState, useEffect } from "react";

export const TelemetryDataContext = createContext();

export const TelemetryDataProvider = ({ children }) => {
  const [data, setData] = useState([]);
  const [dataIsLoaded, setDataIsLoaded] = useState(false);

  useEffect(() => {
    const fetchData = () => {
      fetch("http://127.0.0.1:8000/telemetry/")
        .then((res) => res.json())
        .then((json) => {
          setData(
            json.map((item) => ({
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
            }))
          );
          setDataIsLoaded(true);
        })
        .catch((error) => console.error("Error fetching data:", error));
    };

    return () => fetchData(); // Cleanup on unmount
  }, []);

  return (
    <TelemetryDataContext.Provider value={{ data, dataIsLoaded }}>
      {children}
    </TelemetryDataContext.Provider>
  );
};
