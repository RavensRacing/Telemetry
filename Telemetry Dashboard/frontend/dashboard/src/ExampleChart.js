import React from "react";
import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";

const data = [
  { name: "Red", value: 12 },
  { name: "Blue", value: 19 },
  { name: "Yellow", value: 3 },
  { name: "Green", value: 5 },
  { name: "Purple", value: 2 },
  { name: "Orange", value: 3 },
];

const Mybarchart = () => (
  <div style={{ width: "100%", height: 300 }}>
    <ResponsiveContainer>
      <LineChart data={data}>
        <XAxis dataKey="name" />
        <YAxis />
        <Tooltip />
        <Line dataKey="value" fill="#8884d8" />
      </LineChart>
    </ResponsiveContainer>
  </div>
);

export default Mybarchart;
