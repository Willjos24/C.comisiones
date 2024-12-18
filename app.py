from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas las rutas

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calcular_comision', methods=['POST'])
def calcular_comision():
    data = request.get_json()
    monto_ventas = data.get('monto_ventas')
    porcentaje_comision = data.get('porcentaje_comision')

    if monto_ventas is None or porcentaje_comision is None:
        return jsonify({'error': 'Datos incompletos'}), 400

    try:
        monto_ventas = float(monto_ventas)
        porcentaje_comision = float(porcentaje_comision)

        comision = monto_ventas * (porcentaje_comision / 100)
        return jsonify({'comision': comision}), 200

    except ValueError:
        return jsonify({'error': 'Valores inválidos'}), 400

if __name__ == '__main__':
    app.run(debug=True)
