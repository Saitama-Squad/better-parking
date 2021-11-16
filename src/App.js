import React, { useState, useEffect } from "react";
import "./App.css";
import Floor from "./Floor";
import Login from "./Login";
import Settings from "./Settings";

function App() {
    const [listening, setListening] = useState(false);
    const [floor, setFloor] = useState(1);
    const [page, setPage] = useState("login");
    const [vacancies, setVacancies] = useState({});

    useEffect(() => {
        let vacancy = {};
        for (let i = 0; i < 5; ++i) {
            vacancy[i] = {};
            for (let j = 0; j < 132; ++j) {
                vacancy[i][j] = 1;
            }
        }
        setVacancies(vacancy);
    }, []);

    useEffect(() => {
        if (!listening) {
            const events = new EventSource(
                "https://better-parking-backup.herokuapp.com/events",
                { withCredentials: true }
            );

            events.onmessage = async (event) => {
                console.log(event);
                const parsedData = JSON.parse(event.data);
                let { vacant, floor, id } = parsedData;
                vacant = parseInt(vacant);
                floor = parseInt(floor);
                id = parseInt(id);
                console.log(vacant, floor, id);

                console.log(vacancies);
                await setVacancies((data) => {
                    data[floor - 1][id] = vacant;
                    return data;
                });
                console.log(vacancies);
            };

            setListening(true);
        }
    }, [listening]);

    const changePage = () => {
        if (page === "floors")
            return (
                <Floor
                    setFloor={setFloor}
                    floor={floor}
                    vacancies={vacancies}
                    appStart={listening}
                    setPage={setPage}
                />
            );
        else if (page === "settings") return <Settings setPage={setPage} />;
        else return <Login setPage={setPage} />;
    };
    return <div className="font-montserrat">{changePage()}</div>;
}

export default App;
