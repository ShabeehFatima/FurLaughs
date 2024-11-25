import React, {useState, useEffect} from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [pun, setPun] = useState("");
  const [error, setError] = useState("");

  //Fetch a randmom pun
  const fetchRandomPun = async() => {
    try{
      const response = await axios.get("/puns/random");  //Backend API endpoint
      setPun(response.data.pun);
      setError("");
    }
    catch (err) {
      setError("Oops! Couldn't fetch a pun. Try Again!");
    }
  };
  useEffect(() => {
    fetchRandomPun();
  }, []);

  return(
    <div className="app-container">
    <h1 className="title">FurLaughs</h1>
    <div className="content">
      {error ? (
        <p className="error">{error}</p>
      ) : (
        <p className="pun">{pun || "Fetching a pun for you..."}</p>
      )}
      <button className="fetch-button" onClick={fetchRandomPun}>
        Get Another Pun
      </button>
    </div>
  </div>
);
}

export default App;