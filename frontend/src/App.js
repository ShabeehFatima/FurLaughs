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
      setError("Could not fetch pun. Please try again later!");
    }
  };
  useEffect(() => {
    fetchRandomPun();
  }, []);

  return(
    <div style = {{textAlign : "center", marginTop : "50px"}}>
      <h1>Fur Laughs</h1>
      {error ? (
        <p style = {{color : "Red", }} > {error}</p>
      ) : ( 
        <p style = {{fontSize : "20px"}} > {pun}</p>
      )}
      <button onClick = {fetchRandomPun} style = {{marginTop: "20px" , padding : "10px 20px", fontSize : "16px"}}>Get Another Pun</button>
    </div>
  );
}

export default App;