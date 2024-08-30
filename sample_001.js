const express = require('express');
const axios = require('axios');
const jwt = require('jsonwebtoken');
const bcrypt = require('bcryptjs');

const app = express();
const PORT = 3000;

app.use(express.json());

const users = {}; // Простая база данных пользователей

const SECRET_KEY = 'your_secret_key';

// Регистрация нового пользователя
app.post('/register', async (req, res) => {
    const { username, password } = req.body;
    if (users[username]) {
        return res.status(400).json({ message: 'User already exists' });
    }
    const hashedPassword = await bcrypt.hash(password, 10);
    users[username] = hashedPassword;
    res.status(201).json({ message: 'User registered successfully' });
});

// Авторизация пользователя
app.post('/login', async (req, res) => {
    const { username, password } = req.body;
    const user = users[username];
    if (!user || !(await bcrypt.compare(password, user))) {
        return res.status(401).json({ message: 'Invalid credentials' });
    }
    const token = jwt.sign({ username }, SECRET_KEY, { expiresIn: '1h' });
    res.json({ token });
});

// Middleware для проверки JWT токена
function authenticateToken(req, res, next) {
    const token = req.headers['authorization'];
    if (!token) return res.sendStatus(401);

    jwt.verify(token, SECRET_KEY, (err, user) => {
        if (err) return res.sendStatus(403);
        req.user = user;
        next();
    });
}

// Шаг 3: Создание endpoint'ов оберточного API для управления беспилотником
app.post('/drone-control', authenticateToken, async (req, res) => {
    try {
        const response = await axios.post('http://external-drone-api.com/control', req.body);
        res.json(response.data);
    } catch (error) {
        res.status(500).json({ message: 'Error communicating with drone API', error: error.message });
    }
});

app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${port}`);
});