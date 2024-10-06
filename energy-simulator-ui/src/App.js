import React from 'react';
import './App.css';
import InputForm from '../components/inputForm';  // Import from components folder

function App() {
    return (
        <div className="App">
            <h1>Energy Transition Simulator</h1>
            <InputForm />  {/* Render the form */}
        </div>
    );
}

export default App;
