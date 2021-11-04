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
    let vacancy = {};
    for (let i = 0; i < 5; ++i) {
      vacancy[i] = {};
      for (let j = 0; j < 33; ++j) {
        vacancy[i][j] = 1;
      }
    }
    setVacancies(vacancy);
  }, []);

  useEffect(() => {
    if (!listening) {
      const events = new EventSource("http://localhost:5002/events");

      events.onmessage = (event) => {
        const parsedData = JSON.parse(event.data);
        let { vacant, floor, id } = parsedData;
        vacant = parseInt(vacant);
        floor = parseInt(floor);
        id = parseInt(id);
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
    <div className="font-montserrat">
      {user === "" ? (
        <Login setUser={setUser} />
      ) : (
        <Floor setFloor={setFloor} floor={floor} vacancies={vacancies} />
      )}
    </div>
  );
}

export default App;
