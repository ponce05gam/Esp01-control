from flask import Flask

app = Flask(__name__)
led_status = "off"

@app.route("/on")
def encender():
    global led_status
    led_status = "on"
    print("LED encendido vía /on")  # Esto aparece en logs
    return "LED está ENCENDIDO"

@app.route("/off")
def apagar():
    global led_status
    led_status = "off"
    print("LED apagado vía /off")  # Esto aparece en logs
    return "LED está APAGADO"

@app.route("/status")
def status():
    print(f"Consulta estado LED: {led_status}")
    if led_status == "on":
        return "LED está ENCENDIDO"
    else:
        return "LED está APAGADO"
