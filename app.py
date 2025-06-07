from flask import Flask

app = Flask(__name__)
estado_led = "apagado"

@app.route("/encender")
def encender():
    global estado_led
    estado_led = "encendido"
    return "led encendido"

@app.route("/apagar")
def apagar():
    global estado_led
    estado_led = "apagado"
    return "led apagado"

@app.route("/status")
def status():
    return f"led {estado_led}"
