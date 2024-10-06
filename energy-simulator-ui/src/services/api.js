import axios from 'axios';

const API_URL = 'http://localhost:5000';  // Flask server

export const runSimulation = (data) => {
    return axios.post(`${API_URL}/simulate`, data);  // Ensure it's POST
};
