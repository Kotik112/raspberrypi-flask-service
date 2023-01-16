from flask import Flask, render_template, request
from utils.Bridge import Bridge
from utils.helpers import sort_lights, rgb_to_xy

app = Flask(__name__)

light_list = []  # List of all lights

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/on/<string:room>", methods=["POST"])
def turn_on(room):
    global light_list
    bridge = Bridge()
    light_list = bridge.lights
    lights_to_control = sort_lights(light_list, room)
    for light in lights_to_control:
        light.on = True
    return "", 204

@app.route("/off/<string:room>", methods=["POST"])
def turn_off(room):
    global light_list
    bridge = Bridge()
    light_list = bridge.lights
    lights_to_control = sort_lights(light_list, room)
    for light in lights_to_control:
        light.on = False
    return "", 204

@app.route("/brightness/<string:room>/<int:level>", methods=["POST"])
def set_brightness(room, level):
    global light_list
    bridge = Bridge()
    light_list = bridge.lights
    lights_to_control = sort_lights(light_list, room)
    for i in range(len(lights_to_control)):
        bridge.set_brightness(lights_to_control[i].light_id, level)
    return "", 204

@app.route("/color/<string:room>/<int:r>/<int:g>/<int:b>", methods=["POST"])
def set_color(room, r, g, b):
    global light_list
    bridge = Bridge()
    light_list = bridge.lights
    lights_to_control = sort_lights(light_list, room)
    for i in range(len(lights_to_control)):
        xy = rgb_to_xy(r, g, b)
        bridge.set_color(lights_to_control[i].light_id, xy)
    return "", 204
