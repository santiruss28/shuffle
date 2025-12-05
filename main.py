from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

ARCHIVO = "estado.json"

def cargar_estado():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r") as f:
            return json.load(f)
    return {"ultimo": None}

def guardar_estado(data):
    with open(ARCHIVO, "w") as f:
        json.dump(data, f)

@app.route("/ultimo", methods=["GET"])
def obtener_ultimo():
    estado = cargar_estado()
    return jsonify(estado)

@app.route("/nuevo", methods=["POST"])
def guardar_nuevo():
    nuevo = request.json.get("usuario")
    if not nuevo:
        return jsonify({"error": "Falta 'usuario' en JSON"}), 400
    guardar_estado({"ultimo": nuevo})
    return jsonify({"status": "ok", "usuario": nuevo})

app.run(host="0.0.0.0", port=10000)

