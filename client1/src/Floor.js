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
          className="bg-gray-100 border-2 border-solid border-gray-900 p-1 text-lg text-center w-8 h-8"
          style={{ backgroundColor: colors[vacant] }}
        ></div>
      );
    }
    return res;
  };

  return (
    <div>
      <h1 className="text-5xl text-center">Car Parking</h1>
      <h2 className='flex flex-col justify-center items-center w-full'>
        Floor {floor}
        <div className="flex w-full justify-around items-center">
          {floor > 1 ? (
            <button onClick={() => FloorChange("l")} className="text-xl bg-gray-500 text-white px-5">
              Previous
            </button>
          ) : (
            <></>
          )}
          {floor < 5 ? (
            <button onClick={() => FloorChange("r")} className="text-xl bg-gray-500 text-white px-5">
              Next
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
