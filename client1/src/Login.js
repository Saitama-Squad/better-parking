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

      <form action="/action_page.php" method="post">
        <div className="imgcontainer">
          <img src={Avatar} alt="Avatar" className="avatar" />
        </div>

        <div className="container">
          <label htmlFor="uname">
            <b>Username</b>
          </label>
          <input
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
            type="password"
            placeholder="Enter Password"
            name="psw"
            method="post"
            required
          />

          <button type="submit" className="loginbutton" onClick={loginHandler}>
            Login
          </button>
          <label>
            <input type="checkbox" checked="checked" name="remember" /> Remember
            me
          </label>
        </div>

        <div className="container" style={{ backgroundColor: "#f1f1f1" }}>
          <button type="button" className="cancelbtn">
            Register
          </button>
          <span className="psw">
            <a className="fgp" href="/">
              Forgot password?
            </a>
          </span>
        </div>
      </form>
    </div>
  );
};

export default Login;
