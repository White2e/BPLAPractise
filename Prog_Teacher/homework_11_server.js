// подключаем библиотеки
const express = require('express');
const jwt = require('jsonwebtoken');

// инициализируем
const app = express();
const port = 3000;
const SECRET_KEY = 'my_secret';

app.use(express.json());
// тут у нас токен
let token = null;

// Получение токена (простая регистрации)
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


// Простой интерфейс управления беспилотником
app.post('/drone', verifyToken, (req, res) => {
  const { command } = req.body;
  res.send(`Дрон получил команду: ${command}`);
});

app.listen(port, () => {
  console.log(`Сервер запущен: http://localhost:${port}`);
});
