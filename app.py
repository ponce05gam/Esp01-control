from flask import Flask, request

app = Flask(__name__)

led_state = False

@app.route('/on')
def led_on():
    global led_state
    led_state = True
    print("LED ENCENDIDO")
    return "LED ENCENDIDO"

@app.route('/off')
def led_off():
    global led_state
    led_state = False
    print("LED APAGADO")
    return "LED APAGADO"

@app.route('/status')
def led_status():
    return "LED está " + ("ENCENDIDO" if led_state else "APAGADO")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
