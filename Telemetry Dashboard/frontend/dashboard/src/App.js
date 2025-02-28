import React, { useState, useEffect } from 'react';
import './App.css';
import Mybarchart from './ExampleChart';

function App() {
  const [items, setItems] = useState([]);
  const [dataIsLoaded, setDataIsLoaded] = useState(false);

  useEffect(() => {
      fetch("http://127.0.0.1:8000/telemetry/")
          .then((res) => res.json())
          .then((json) => {
              setItems(json);
              setDataIsLoaded(true);
          });
  }, []);

  if (!dataIsLoaded) return <h1>Please wait some time...</h1>;

  return (
        <div className="App">
          <h2>Bar Chart:</h2>
          <Mybarchart />
        <h1>API Data Fetch Example</h1>
        <div className="container">
            {items.map((item) => (
                <div className="item" key={item.id}>
                    <p><strong>Username:</strong> {item.username}</p>
                    <p><strong>Name:</strong> {item.name}</p>
                    <p><strong>Email:</strong> {item.email}</p>
                </div>
            ))}
        </div>
    </div>
  );
}

export default App;
