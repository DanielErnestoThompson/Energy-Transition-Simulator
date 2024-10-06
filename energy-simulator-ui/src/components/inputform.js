import React, { useState } from 'react';
import { runSimulation } from '../services/api';  // Axios API call

const InputForm = () => {
    const [carbonPrice, setCarbonPrice] = useState(0);
    const [subsidies, setSubsidies] = useState(0);
    const [result, setResult] = useState(null);  // State to store the result

    // Handle form submission
    const handleSubmit = (event) => {
        event.preventDefault();
    
        const simulationData = {
            carbon_price: carbonPrice,
            subsidies: subsidies
        };
    
        runSimulation(simulationData)  // Ensure this calls the POST request
            .then(response => {
                setResult(response.data);  // Display the result
            })
            .catch(error => {
                console.error('Error running simulation:', error);
            });
    };
    

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <label>
                    Carbon Price:
                    <input 
                        type="number" 
                        value={carbonPrice} 
                        onChange={e => setCarbonPrice(e.target.value)} 
                    />
                </label>
                <label>
                    Renewable Subsidies:
                    <input 
                        type="number" 
                        value={subsidies} 
                        onChange={e => setSubsidies(e.target.value)} 
                    />
                </label>
                <button type="submit">Simulate</button>
            </form>

            {/* Display the result */}
            {result && (
                <div>
                    <h2>Simulation Result:</h2>
                    <p>Carbon Price Received: {result.carbon_price_received}</p>
                    <p>Subsidies Received: {result.subsidies_received}</p>
                    <p>Simulation Output: {result.simulation_output}</p>
                </div>
            )}
        </div>
    );
};

export default InputForm;
