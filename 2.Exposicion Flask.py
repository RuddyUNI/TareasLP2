from flask import Flask, request, jsonify

app = Flask(__name__)

# Ruta básica - "Hello, World!"
@app.route('/')
def hello_world():
    return "Hello, World!"

# Explicación de app.run(debug=True)
# - Permite que el servidor se reinicie automáticamente en caso de cambios.
# - Muestra errores en el navegador si ocurre un fallo.

# Rutas con diferentes métodos HTTP
@app.route('/greet/<name>', methods=['GET'])
def greet(name):
    return f"Hello, {name}!"

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.json  # Recibe datos en formato JSON
    return jsonify({"message": "Datos recibidos", "data": data})

@app.route('/update', methods=['PUT'])
def update_data():
    data = request.json
    return jsonify({"message": "Datos actualizados", "data": data})

@app.route('/delete/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    return jsonify({"message": f"Elemento {item_id} eliminado"})

if __name__ == '_main_':
    app.run(debug=True)