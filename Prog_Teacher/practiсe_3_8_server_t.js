const express = require('express');
const arDrone = require("ar-drone");

const app = express();

const drone1 = arDrone.createClient(); // 192.168.1.1
const drone2 = arDrone.createClient({ip: '192.168.1.2'});

drone1.on("navdata", (data) => {
    console.log('Данные от дрона 1:', data);
});

app.get('/time', (req, res) => {
    const currentTime = new Date();
    res.json({time: currentTime});
});

app.get('/1/takeoff', (req, res) => {
    drone1.takeoff();
    res.json({Drone_1: "Взлетел"});
    console.log('Дрона 1 Взлетел');
});

const PORT = 3000;

app.listen(PORT, () => {
    console.log("Сервер запущен!")
})