import React from "react";

const Settings = ({ setPage }) => {
  const goBack = () => {
    setPage("floors");
  };
  return (
    <div>
      <button onClick={goBack}>Go Back</button>
      Settings
    </div>
  );
};

export default Settings;
