import React from "react";

const Floor = ({ setFloor, floor, vacancies }) => {
  const colors = ["red", "green"];

  const FloorChange = (dir) => {
    if (dir === "l") setFloor(floor - 1);
    else setFloor(floor + 1);
  };

  const Tiles = () => {
    const res = [];
    for (let i = 0; i < 30; ++i) {
      let vacant = vacancies[floor - 1][i];
      res.push(
        <div
          className="grid-item"
          style={{ backgroundColor: colors[vacant] }}
        ></div>
      );
    }
    return res;
  };

  return (
    <div>
      <h1>Car Parking</h1>
      <h2 className="floors">
        Floor {floor}
        <div className="navs">
          {floor > 1 ? (
            <button onClick={() => FloorChange("l")}>
              <i class="glyphicon glyphicon-chevron-left next1"></i>
            </button>
          ) : (
            <></>
          )}
          {floor < 5 ? (
            <button onClick={() => FloorChange("r")}>
              <i class="glyphicon glyphicon-chevron-right next1"></i>
            </button>
          ) : (
            <></>
          )}
        </div>
      </h2>
      <div class="grid-container">{Tiles().map((e) => e)}</div>
    </div>
  );
};

export default Floor;
