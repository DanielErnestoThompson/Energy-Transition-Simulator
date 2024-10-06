import axios from 'axios';

const API_URL = 'http://localhost:5000';  // Update this if your Flask backend is hosted elsewhere

// Function to send simulation data to the backend
export const runSimulation = (data) => {
    return axios.post(`${API_URL}/simulate`, data);
};
