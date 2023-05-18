import json
from flask import Flask, request
from bd import lojas

app = Flask(__name__)

def jsonify_custom(data):
    response = app.response_class(
        response=json.dumps(data, sort_keys=False),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/', methods=['GET'])
def loja():
    return jsonify_custom(lojas)


@app.route('/loja/forms', methods=['POST'])
def adicionar_loja():
    loja = request.json
    lojas.append(loja)
    return "Loja cadastrada com sucesso!"

@app.route('/loja/<int:id>', methods=['GET'])
def get_loja_by_id(id):
    for loja in lojas:
        if loja['id'] == id:
            return jsonify_custom(loja)
    return "Loja não encontrada!"

@app.route('/loja/<int:id>', methods=['DELETE'])
def excluir_loja(id):
    for loja in lojas:
        if loja['id'] == id:
            lojas.remove(loja)
            return "Loja excluída com sucesso!"
    return "Loja não encontrada!"

if __name__ == '__main__':
    app.run()