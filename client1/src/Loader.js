import React from "react";
import "./Loader.css";

const Loader = ({ show }) => {
    return (
        <div
            className={`${
                show ? "block" : "hidden"
            } loader-par flex justify-center items-center w-screen h-screen absolute`}
        >
            <div className="loader">Loading...</div>
        </div>
    );
};

export default Loader;
