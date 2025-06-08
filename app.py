from flask import Flask

app = Flask(__name__)
led_status = "off"

@app.route("/on")
def encender():
    global led_status
    led_status = "on"
    return "LED encendido"

@app.route("/off")
def apagar():
    global led_status
    led_status = "off"
    return "LED apagado"

@app.route("/status")
def status():
    global led_status
    if led_status == "on":
        return "LED ENCENDIDO"
    else:
        return "LED APAGADO"
