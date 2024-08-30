const express = require('express');
const app = express();

app.get('/time', (req, res) => {
    let currentTime = new Date();
    let formattedTime;
    formattedTime = currentTime.toLocaleString();
    res.json({ time: formattedTime });
});

const port = 3000;
app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
