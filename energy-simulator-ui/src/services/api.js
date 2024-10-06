import axios from 'axios';

const API_URL = 'http://localhost:5000';  // Your Flask backend's URL

export const runSimulation = (data) => {
    return axios.post(`${API_URL}/simulate`, data);
};
