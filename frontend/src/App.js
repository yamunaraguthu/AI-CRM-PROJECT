import React, { useState, useEffect } from "react";
import axios from "axios";

function App() {
  const [doctor, setDoctor] = useState("");
  const [notes, setNotes] = useState("");
  const [response, setResponse] = useState("");
  const [history, setHistory] = useState([]);

  // Fetch history
  const fetchHistory = async () => {
    const res = await fetch("http://127.0.0.1:8000/history");
    const data = await res.json();
    setHistory(data);
  };

  useEffect(() => {
    fetchHistory();
  }, []);

  // Submit new data
  const sendData = async () => {
    try {
      const res = await axios.post("http://127.0.0.1:8000/log", {
        doctor_name: doctor,
        date: "today",
        notes: notes
      });

      setResponse(res.data.summary);
      fetchHistory(); // refresh history

    } catch (err) {
      console.log(err);
      setResponse("Error connecting to backend");
    }
  };

  // ✏️ Edit function
  const handleEdit = async (id, oldNotes) => {
    const newNotes = prompt("Edit notes:", oldNotes);

    if (!newNotes) return;

    try {
      await axios.put(`http://127.0.0.1:8000/edit/${id}`, {
        notes: newNotes
      });

      fetchHistory(); // refresh after edit
    } catch (err) {
      console.log(err);
      alert("Error updating");
    }
  };

  return (
    <div style={{ padding: "30px", fontFamily: "Arial" }}>
      <h2>AI CRM - Doctor Interaction</h2>

      <input
        placeholder="Doctor Name"
        value={doctor}
        onChange={(e) => setDoctor(e.target.value)}
      />
      <br /><br />

      <textarea
        placeholder="Enter interaction notes..."
        value={notes}
        onChange={(e) => setNotes(e.target.value)}
        rows="4"
        cols="40"
      />
      <br /><br />

      <button onClick={sendData}>Submit</button>

      <h3>AI Summary:</h3>
      <p>{response}</p>

      <h3>History:</h3>

      {history.map((item) => (
        <div key={item.id} style={{ border: "1px solid black", margin: "10px", padding: "10px" }}>
          <p><b>Doctor:</b> {item.doctor_name}</p>
          <p><b>Notes:</b> {item.notes}</p>
          <p><b>Summary:</b> {item.summary}</p>

          <button onClick={() => handleEdit(item.id, item.notes)}>
            Edit
          </button>
        </div>
      ))}
    </div>
  );
}

export default App;