import React from "react";
const Loader = ({ show }) => {
    return (
        <div
            className={`${show ? "block" : "hidden"
                } loader-par flex justify-center items-center w-screen h-screen absolute`}
        >
        </div>
    );
};

export default Loader;