from flask import Flask
app = Flask(_name_)

# Estado global (se pierde si el servidor se reinicia)
estado_actual = {"estado": "APAGADO"}

@app.route('/encender')
def encender():
    estado_actual["estado"] = "ENCENDIDO"
    return "Estado cambiado a ENCENDIDO"

@app.route('/apagar')
def apagar():
    estado_actual["estado"] = "APAGADO"
    return "Estado cambiado a APAGADO"

@app.route('/status')
def status():
    return estado_actual["estado"]

