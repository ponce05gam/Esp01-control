estado_led = "APAGADO"  # Estado inicial

@app.route('/encender')
def encender():
    global estado_led
    estado_led = "ENCENDIDO"
    return "LED encendido"

@app.route('/apagar')
def apagar():
    global estado_led
    estado_led = "APAGADO"
    return "LED apagado"

@app.route('/status')
def status():
    return estado_led
