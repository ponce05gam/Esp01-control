from flask import Flask
import os

app = Flask(__name__)

ARCHIVO_ESTADO = "estado.txt"

def guardar_estado(estado):
    with open(ARCHIVO_ESTADO, "w") as archivo:
        archivo.write(estado)

def leer_estado():
    if not os.path.exists(ARCHIVO_ESTADO):
        return "APAGADO"  # Por defecto
    with open(ARCHIVO_ESTADO, "r") as archivo:
        return archivo.read()

@app.route("/encender")
def encender():
    guardar_estado("ENCENDIDO")
    return "led encendido"

@app.route("/apagar")
def apagar():
    guardar_estado("APAGADO")
    return "led apagado"

@app.route("/status")
def status():
    return leer_estado()
