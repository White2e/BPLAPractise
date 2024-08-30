const express = require('express');
const arDrone = require("ar-drone");
const axios = require('axios');

const app = express();
const PORT = 3000;

const drone1 = arDrone.createClient();

app.use(express.json());


drone1.on("navdata", (data) => {
    console.log('Data from Drone1: ', data);
});


app.get('/drone1/takeoff', (req, res) => {
    drone1.takeoff();
    res.json({message: 'Drone 1 has taken off'});
});


app.get('/drone1/land', (req, res) => {
    drone1.land();
    res.json({message: 'Drone 1 has landed'});
});


app.get('/', (req, res) => {
    res.send('API wrapper is working!');
});


app.get('/time', (req, res) => {
    // Получаем параметр форматирования, если он указан
    const format = req.query.format || 'iso';

    let currentTime = new Date();

    let formattedTime;
    if (format === 'iso') {
        formattedTime = currentTime.toISOString();
    } else if (format === 'utc') {
        formattedTime = currentTime.toUTCString();
    } else if (format === 'locale') {
        formattedTime = currentTime.toLocaleString();
    } else {
        formattedTime = currentTime.toString();
    }

    res.json({ time: formattedTime });
});


app.post('/drone-control', async (req, res) => {
    try {
        const response = await axios.post('http://localhost:5000/drone-control', req.body);
        res.json(response.data);
    } catch (error) {
        res.status(500).send(error.message);
    }
});


app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
