from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hola desde Render y Flask!"

@app.route('/status')
def status():
    return "ENCENDIDO"

@app.route('/apagar')
def apagar():
    return "APAGADO"

if __name__ == '__main__':
    # Esto solo se ejecuta si corres python app.py localmente
    app.run(host='0.0.0.0', port=5000, debug=True)

