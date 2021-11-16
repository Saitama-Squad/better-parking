import React,{useState} from "react";
import Avatar from "./images/avatar.png";
import Font from "react-font";
import Loader from "./Loader";
import { collection, query, where, getDocs } from "firebase/firestore";
import { getAuth, signInWithEmailAndPassword } from "firebase/auth";
import { getFirestore } from "firebase/firestore";
import firebase from "./firebaseConfig";
const Login = ({ setPage }) => {
  const db = getFirestore()
  const [loader, setLoader] = useState(false);
  const [error, setError] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const loginHandler = async(e) => {
    e.preventDefault();
    setLoader(true);
    setError("")
    console.log(process.env.REACT_APP_API_KEY)
    if (username.length === 0) {
      setError("Enter Username")
    }
    else if (password.length === 0) {
      setError("Enter Password")
    }
    else {
      const auth = getAuth();
      try {
        const userCredential = await signInWithEmailAndPassword(
          auth,
          username,
          password
        );
        const user = userCredential.user;
        console.log(user)
      }
      catch {

      }
    }
    setLoader(false);
    //setPage("floors");
  };

  return (
    <div className="relative">
      <Loader show={loader} />
      <div className="h-screen w-screen" style={{
        background:
          "linear-gradient(rgba(0,0,0,0.7),rgba(0,0,0,0.7))",
      }}>
        <div className="px-16 pt-12">
          <Font family="Monoton"><h1 className="text-6xl text-center text-white">Better-Parking Welcomes you</h1></Font>
        </div>
        <form className="flex flex-col justify-around items-center">
          <div className="mt-6 mb-3 flex items-center justify-center">
            <img src={Avatar} alt="Avatar" className="w-4/12 rounded-full" />
          </div>

          <div className="p-4 w-1/2">
            <label htmlFor="uname" className="text-white">
              <b>Username</b>
            </label>
            <input
              className="w-full py-3 px-5 my-2 border-2 border-solid border-gray-200 flex justify-center items-center"
              type="text"
              placeholder="Enter Username"
              name="uname"
              method="post"
              onChange={(event) => {
                setUsername(event.target.value)
              }}
              required
            />

            <label htmlFor="psw" className="text-white">
              <b>Password</b>
            </label>
            <input
              className="w-full py-3 px-5 my-2 border-2 border-solid border-gray-200 flex justify-center items-center"
              type="password"
              placeholder="Enter Password"
              name="psw"
              method="post"
              onChange={(event) => {
                setPassword(event.target.value)
              }}
              required
            />
            <div className="flex justify-center text-red-500 text-lg">
              {error}
            </div>  
            <button
              type="submit"
              className="bg-green-600 text-white py-3 px-5 my-2 mx-0 border-none cursor-pointer w-full hover:opacity-80"
              onClick={loginHandler}
            >
              Login
            </button>
          </div>
        </form>
      </div>
      
    </div>
  );
};

export default Login;
