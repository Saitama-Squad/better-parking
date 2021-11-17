// Import the functions you need from the SDKs you need
import firebase from "firebase/compat/app";
import "firebase/compat/firestore";
import 'firebase/compat/auth';
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyBksIoBFT24_VbWz19mWcAXAPkjWpqznXw",
    authDomain: "better-parking.firebaseapp.com",
    projectId: "better-parking",
    storageBucket: "better-parking.appspot.com",
    messagingSenderId: "841979575193",
    appId: "1:841979575193:web:81616e002ed7c4379ff108",
    measurementId: "G-BYM6MNK0MX"
};


// Initialize Firebase
firebase.initializeApp(firebaseConfig);

export default firebase;