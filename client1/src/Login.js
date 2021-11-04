import React from "react";
import Avatar from "./images/avatar.png";

const Login = ({ setUser }) => {
  const loginHandler = (e) => {
    e.preventDefault();
    setUser("admin");
  };

  return (
    <div>
      <h1>Better Parking Welcomes You!!!</h1>

      <form className="border-2 border-black border-solid flex flex-col justify-around items-center">
        <div className="mt-6 mb-3 flex items-center justify-center">
          <img src={Avatar} alt="Avatar" className="w-4/12 rounded-full" />
        </div>

        <div className="p-4 w-full">
          <label htmlFor="uname">
            <b>Username</b>
          </label>
          <input
            className="w-full py-3 px-5 my-2 border-2 border-solid border-gray-200 flex justify-center items-center"
            type="text"
            placeholder="Enter Username"
            name="uname"
            method="post"
            required
          />

          <label htmlFor="psw">
            <b>Password</b>
          </label>
          <input
            className="w-full py-3 px-5 my-2 border-2 border-solid border-gray-200 flex justify-center items-center"
            type="password"
            placeholder="Enter Password"
            name="psw"
            method="post"
            required
          />

          <button type="submit" className="bg-green-600 text-white py-3 px-5 my-2 mx-0 border-none cursor-pointer w-full hover:opacity-80" onClick={loginHandler}>
            Login
          </button>
          <label>
            <input type="checkbox" checked="checked" name="remember" /> Remember
            me
          </label>
        </div>

        <div className="p-4 flex flex-row w-full items-center justify-around" style={{ backgroundColor: "#f1f1f1" }}>
          <button type="button" className="w-auto py-3 px-4 bg-red-500 text-white">
            Register
          </button>
          <span>
            <a href="/">
              Forgot password?
            </a>
          </span>
        </div>
      </form>
    </div>
  );
};

export default Login;
