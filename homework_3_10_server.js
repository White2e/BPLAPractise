const express = require('express');
const app = express();

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

const port = 3000;
app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
