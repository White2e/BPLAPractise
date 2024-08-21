from pyinstrument  import Profiler
from flask import Flask, request, g, make_response
import math
import time
import random

app = Flask(__name__)


def get_sensor_data():
    time.sleep(0.05)  # Simulating sensor data fetching delay
    return {"altitude": random.randint(0, 500),
            "speed": random.randint(0, 70)}


def process(data):
    time.sleep(0.1)  # Simulating data process delay
    return {
        "altitude": data["altitude"] / 39.37,  # перевод дюймов в метры
        "speed": data["speed"] * 0.609  # перевод милей/ч в километры/ч
    }


def make_decision(data):
    time.sleep(0.2)  # Simulating data decision process delay
    if data['altitude'] < 50:
        return "Поднимаемся выше"
    elif data['altitude'] > 100:
        return "Опускаемся ниже"
    else:
        return "Садимся"


def motor_control(decision):
    time.sleep(0.2)  # Simulating data decision process delay
    return f"Задача мотора {decision}"


@app.route('/', methods=['GET'])
def index():
    data = get_sensor_data()
    processed_data = process(data)
    decision = make_decision(processed_data)
    motor_command = motor_control(decision)
    return f"Команда на дрон: {motor_command}"


@app.before_request
def before_request():
    #if "profile" in request.args:
    g.is_profiling = "profile" in request.args
    if g.is_profiling:
        g.profile = Profiler()
        g.profile.start()

@app.after_request
def after_request(response):
    if g.is_profiling:
        g.profile.stop()
        output_html = g.profile.output_html()
        return make_response(output_html, 200)
    return response


if __name__ == '__main__':
    app.run(debug=True)
