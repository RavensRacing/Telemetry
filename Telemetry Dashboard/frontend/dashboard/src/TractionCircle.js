import React, {useContext } from "react";
import { Scatter, XAxis, YAxis, Tooltip, ResponsiveContainer, ScatterChart } from "recharts";
import { TelemetryDataContext } from "./DataProvider";

const TractionCircle = () => {

    const { data, dataIsLoaded } = useContext(TelemetryDataContext);

  if (!dataIsLoaded) {
    return <p>Loading...</p>;
  }

  console.log(data);

  return (
    <div style={{ width: "100%", height: 1000 }}>
      <ResponsiveContainer>
        <ScatterChart>
          <XAxis type="number" dataKey="vertical_acc" />
          <YAxis type="number" dataKey="lateral_acc" />
          <Tooltip />
          <Scatter data={data} fill="green"/>
          <circle cx={0} cy={0} r={1} fill="none" stroke="red" strokeWidth={2} />
        </ScatterChart>
      </ResponsiveContainer>
    </div>
  );
};

export default TractionCircle;
  