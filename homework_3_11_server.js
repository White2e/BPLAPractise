Установите необходимые зависимости, такие как express для создания сервера, и axios для отправки HTTP-запросов:

npm install express axios

Создайте файл server.js в корневой директории проекта.
Импортируйте express и создайте экземпляр приложения

const express = require('express');
const axios = require('axios');
const app = express();
const PORT = 3000;

app.use(express.json());

Настройте маршруты API. Например, для тестирования можно создать простой маршрут:

app.get('/', (req, res) => {
    res.send('API wrapper is working!');
});

Запустите сервер:

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});

Настройка маршрутов для взаимодействия с Python API:

Определите маршруты, которые будут отправлять запросы к вашему Python API. Пример:

app.post('/drone-control', async (req, res) => {
    try {
        const response = await axios.post('http://localhost:5000/drone', req.body);
        res.json(response.data);
    } catch (error) {
        res.status(500).send(error.message);
    }
});









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
