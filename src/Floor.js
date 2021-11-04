import React from "react";
import Vacantb from "./images/vacant/b.jpg";
import Vacantt from "./images/vacant/t.jpg";
import car1t from "./images/occupied/1t.jpg";
import car2t from "./images/occupied/2t.jpg";
import car1b from "./images/occupied/1b.jpg";
import car2b from "./images/occupied/2b.jpg";
import car3t from "./images/occupied/3t.jpg";
import RoadLeft from "./images/road/l.jpg";
import RoadRight from "./images/road/r.jpg";

const Floor = ({ setFloor, floor, vacancies }) => {
  const FloorChange = (dir) => {
    if (dir === "l") setFloor(floor - 1);
    else setFloor(floor + 1);
  };

  const Tiles = (dir, start) => {
    const res = [];
    const carst = [car1t, car2t, car3t],
      carsb = [car1b, car2b];
    for (let i = start, j = 0; i < start + 33; ++i, ++j) {
      let vacant = vacancies[floor - 1][j];

      // let element;
      // element = document.getElementById(i);
      // if (
      //   element &&
      //   element.attributes &&
      //   element.attributes.alt &&
      //   element.attributes.alt.nodeValue
      // ) {
      //   const prevVacant = element.attributes.alt.nodeValue == "vacant" ? 1 : 0;
      //   console.log(prevVacant, vacant);
        // if (prevVacant == vacant && !prevVacant) {
        //   res.push(element);
        //   continue;
        // }
      // }

      if (vacant) {
        const file = dir === "t" ? Vacantt : Vacantb;
        res.push(<img src={file} alt="vacant" id={i} />);
      } else {
        if (dir === "t") {
          const file = carst[Math.floor(Math.random() * 3)];
          res.push(<img className="" src={file} alt="occupied" id={i} />);
        } else {
          const file = carsb[Math.floor(Math.random() * 2)];
          res.push(<img className="" src={file} alt="occupied" id={i} />);
        }
      }
    }
    return res;
  };

  return (
    <div className="overflow-hidden">
      <div className="header flex flex-row justify-between items-center mx-2 my-2">
        <h2 className="flex justify-start items-center w-full text-5xl">
          Floor {floor}
        </h2>
        <div className="flex w-full justify-end items-center select-none">
          {floor > 1 ? (
            <button
              onClick={() => FloorChange("l")}
              className="text-xl bg-gray-500 text-white px-5 mr-3"
            >
              Previous
            </button>
          ) : (
            <></>
          )}
          {floor < 5 ? (
            <button
              onClick={() => FloorChange("r")}
              className="text-xl bg-gray-500 text-white px-5 mr-3"
            >
              Next
            </button>
          ) : (
            <></>
          )}
        </div>
      </div>
      <div className="carpark border border-black h-full w-full flex flex-col m-auto">
        <div className="row1 flex flex-row">{Tiles("b", 0).map((e) => e)}</div>
        <div className="road-left">
          <img src={RoadLeft} className="w-full h-20" alt="road-left" />
        </div>
        <div className="row2 flex flex-row">{Tiles("t", 33).map((e) => e)}</div>
        <div className="row3 flex flex-row">{Tiles("b", 66).map((e) => e)}</div>
        <div className="road-right">
          <img src={RoadRight} className="w-full h-20" alt="road-right" />
        </div>
        <div className="row4 flex flex-row">{Tiles("t", 99).map((e) => e)}</div>
      </div>
    </div>
  );
};

export default Floor;
