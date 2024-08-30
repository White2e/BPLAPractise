from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

# Setup the Flask-JWT-Extended extension
app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'my_secret_key'
jwt = JWTManager(app)

users = {}


@app.route("/register", methods=["POST"])
def register():
    username = request.json.get('username')
    password = request.json.get('password')
    if username and password:
        if username in users:
            return jsonify({"error": "Пользователь с таким именем уже зарегистрирован"}), 400
        users[username] = password
        return jsonify({"message": f"Пользователь {username} зарегистрирован"}), 201
    else:
        return jsonify({"message": f"Пользователь не задан"}), 400


def register_user(username, password):
    if username and password:
        if username in users:
            return False
        users[username] = password
        return True
    else:
        return False


def login_user(username, password):
    if username not in users or users[username] != password:
        return False
    access_token = create_access_token(identity=username)
    return access_token

# Create a route to authenticate users and return JWTs. The
# create_access_token() function is used to actually generate the JWT.
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username not in users or users[username] != password:
        return jsonify({"msg": "Bad username or password"}), 401
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)


# Protect a route with jwt_required, which will kick out requests
# without a valid JWT present.
@app.route('/drone-control', methods=['POST'])
def control_drone():
    data = request.json
    print(data)
    # отправка команд дрону
    response = send_drone_auth_command(data)
    return jsonify(response)


def send_drone_auth_command(data):
    if data['token'] == '':
        token = ''
    else:
        token = data['token']
    if data['command'] == 'register':
        data['status'] = register_user(data['username'], data['password'])
    if data['command'] == 'login':
        data['token'] = login_user(data['username'], data['password'])
    return data


if __name__ == '__main__':
    app.run(port=5000, debug=True)
