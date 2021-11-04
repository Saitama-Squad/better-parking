import React, { useState, useEffect } from "react";
import "./App.css";
import Floor from "./Floor";
import Login from "./Login";

function App() {
  const [listening, setListening] = useState(false);
  const [user, setUser] = useState("");
  const [floor, setFloor] = useState(1);
  const [vacancies, setVacancies] = useState({});

  useEffect(() => {
    let vacant = {};
    for (let i = 0; i < 5; ++i) {
      vacant[i] = {};
      for (let j = 0; j < 30; ++j) {
        vacant[i][j] = 0;
      }
    }
    setVacancies(vacant);
  }, []);

  useEffect(() => {
    if (!listening) {
      const events = new EventSource("http://localhost:5002/events");

      events.onmessage = (event) => {
        const parsedData = JSON.parse(event.data);
        const { vacant, floor, id } = parsedData;
        console.log(vacant, floor, id);

        setVacancies((data) => {
          data[floor - 1][id] = vacant;
          return { ...data };
        });
      };

      setListening(true);
    }
  }, [listening]);

  return (
    <>
      {user === "" ? (
        <Login setUser={setUser} />
      ) : (
        <Floor setFloor={setFloor} floor={floor} vacancies={vacancies} />
      )}
    </>
  );
}

export default App;
