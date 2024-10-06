import React, { useState } from 'react';
import { runSimulation } from '../services/api';  // Axios call we'll define next

const InputForm = () => {
    const [carbonPrice, setCarbonPrice] = useState(0);
    const [subsidies, setSubsidies] = useState(0);

    const handleSubmit = (event) => {
        event.preventDefault();

        const simulationData = {
            carbon_price: carbonPrice,
            subsidies: subsidies
        };

        runSimulation(simulationData)
            .then(response => {
                console.log('Simulation results:', response.data);
            })
            .catch(error => {
                console.error('Error running simulation:', error);
            });
    };

    return (
        <form onSubmit={handleSubmit}>
            <label>
                Carbon Price:
                <input type="number" value={carbonPrice} onChange={e => setCarbonPrice(e.target.value)} />
            </label>
            <label>
                Renewable Subsidies:
                <input type="number" value={subsidies} onChange={e => setSubsidies(e.target.value)} />
            </label>
            <button type="submit">Simulate</button>
        </form>
    );
};

export default InputForm;
