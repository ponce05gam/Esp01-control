from flask import Flask

app = Flask(__name__)
led_status = "off"

@app.route("/on")
def encender():
    global led_status
    led_status = "on"
    return "LED ENCENDIDO"

@app.route("/off")
def apagar():
    global led_status
    led_status = "off"
    return "LED APAGADO"

@app.route("/status")
def status():
    if led_status == "on":
        return "LED está ENCENDIDO"
    else:
        return "LED está APAGADO"
