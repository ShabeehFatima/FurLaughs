import React, {useState, useEffect} from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [pun, setPun] = useState("");
  const [error, setError] = useState("");
  const [message, setMessage] = useState(""); //Success message for adding pun
  const [newPun, setNewPun] = useState("");  //State for new pun input
  const [showaddPun, setShowAddPun] = useState(false); //State to toggle textbox visbility for new pun


  //Fetch a randmom pun
  const fetchRandomPun = async() => {
    try{
      const response = await axios.get("/puns/random");  //Backend API endpoint
      setPun(response.data.pun);
      setError(""); //Clear any previous error message
    }
    catch (err) {
      setError("Oops! Couldn't fetch a pun. Try Again!");
    }
  };
  useEffect(() => {
    fetchRandomPun();
  }, []);

 //Add a new pun
 const addNewPun = async() => {
  if (!newPun.trim()){
    setError("Please enter a pun before submitting!");
    return
  }

  try{
    const response = await axios.post("/puns/add", {new_pun:newPun});  //Backend API endpoint
    setMessage(response.data.message);
    setError("");
    setNewPun("");
    setShowAddPun(false);
  }
  catch (err) {
    setError("Couldn't add the pun. Please Try Again!");
  }
};
useEffect(() => {
  addNewPun();
}, []);


  return(
    <div className="app-container">
      <h1 className="title">FurLaughs</h1>
      <div className="content">
        {error && <p className="error">{error}</p>}
        {pun && <p className="pun">{pun}</p>}
        {<button className="fetch-button" onClick={fetchRandomPun}>Get Another Pun </button>}
      </div>
      <div className="add-pun-container">
        <button 
          className="toggle-add-button"
          onClick={() =>setShowAddPun(!showaddPun)}
        >
          {showaddPun ? "Cancel" : "Add a new Pun"}
        </button>
      {showaddPun && (
        <div className="add-pun-form">
          <input type="text" placeholder="Enter Your Pun here..." value={newPun} onChange={(e) =>setNewPun(e.target.value)} className="pun-input"/>
          <button onClick={addNewPun} className="add-button">Submit</button>
        </div>
      )}
      {message && <p className="success-message">{message}</p>}
      </div>
    </div>
  );
}

export default App;