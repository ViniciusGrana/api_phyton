
from flask import Flask, jsonify, make_response, request
from bd import Clima


app = Flask('clima')


@app.route("/clima", methods = ["GET"])
def get_clima():
    return Clima


@app.route("/clima/<int:id>", methods =["GET"])
def get_clima_id(id):
    for clima in Clima:
        if clima.get("id") == id:
            return jsonify(clima)
        
@app.route("/clima", methods = ["POST"])
def criar_clima():
    clima = request.json
    Clima.append(clima)
    return make_response(
        jsonify(mensagem ='Carro cadastrado com sucesso',
                clima = clima)
    )

@app.route("/clima/<int:id>", methods = ["PUT"])
def editar_clima(id):
    for indice, clima in enumerate(Clima):
        if clima.get("id")==id:
            Clima[indice].update(editar_clima)
            return jsonify("Editado com sucesso")





@app.route("/clima/<int:id>", methods = ["DELETE"])
def deleta_clima(id):
    for indice, clima in enumerate(Clima):
        if clima.get("id") == id:
            del Clima[indice]
            return jsonify("Clima excluido ")
        

app.run(port=5000, host="localhost")

