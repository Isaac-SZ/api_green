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

@app.route('/loja/<int:id>', methods=['GET'])
def get_loja(id):
    if id in lojas:
        return jsonify_custom(lojas[id])
    else:
        return jsonify_custom({"message": "Loja nao encontrada"}), 404

@app.route('/loja/forms', methods=['POST'])
def adicionar_loja():
    loja = request.json
    lojas.append(loja)
    return "Loja cadastrada com sucesso!"


if __name__ == '__main__':
    app.run()