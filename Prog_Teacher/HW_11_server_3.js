// npm init -y
// npm install express jsonwebtoken
// node название_сервер.js

const express = require('express');
const jwt = require('jsonwebtoken');

const app = express();
const port = 3000;
const SECRET_KEY = 'my_secret';

app.use(express.json());

let token = null;

// Получение токена (вместо логина и регистрации)
app.post('/get-token', (req, res) => {
  token = jwt.sign({ user: 'test_user' }, SECRET_KEY);
  res.json({ token });
});

// Проверка токена
function verifyToken(req, res, next) {
  const authHeader = req.headers['authorization'];
  const authToken = authHeader && authHeader.split(' ')[1];
  if (authToken === token) {
    next();
  } else {
    res.sendStatus(403);
  }
}

// Простой маршрут для проверки
app.get('/hello', verifyToken, (req, res) => {
  res.send('Hello, authenticated user!');
});

// Управление беспилотником
app.post('/drone', verifyToken, (req, res) => {
  const { command } = req.body;
  res.send(`Drone received command: ${command}`);
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
