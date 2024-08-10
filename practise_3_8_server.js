const express = require('express');
const arDrone = require('ar-drone');

const app = express();

const drone1 = arDrone.createClient();
const drone2 = arDrone.createClient({ip: '192.168.1.2'});

drone1.on('navdata', (data) => {
  console.log('Data from Drone1: ', data);
});


app.get('/time', (req, res) => {
  const currentTime = new Date().toLocaleString('en-US', { timeZone: 'America/New_York' });
  res.send(`The current time in New York is: ${currentTime}`);
  console.log(`Request received at ${new Date().toISOString()}`);
  res.json({time: currentTime});
});


app.get('/:droneid/takeoff', (req, res) => {
  drone1.takeoff();
  console.log('Drone 1 is taking off');

  res.json({status: droneid + 'TakeOff'});
});


const PORT = 3000;
app.listen(PORT, () => {
  console.log('Server is running on port 3000');
});