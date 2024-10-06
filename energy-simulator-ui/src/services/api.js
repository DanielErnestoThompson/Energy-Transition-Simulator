import axios from 'axios';

const API_URL = 'http://localhost:5000';  // Make sure Flask is running on this URL and port

export const runSimulation = (data) => {
    // Sending the POST request to /simulate endpoint
    return axios.post(`${API_URL}/simulate`, data);
};
