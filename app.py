import json
import flask

app = flask.Flask(__name__)

lojas = {
    1: {"Nome Fantasia": "Ecoloja", "Razao Social": "Ecoloja SA", "CNPJ": "22.206.183/0001-39", "Endereco": "Rua das Ninfas", "Redes Sociais": "@ecoloja"},
    2: {"Nome Fantasia": "Ecoloja", "Razao Social": "Ecoloja SA", "CNPJ": "22.206.183/0001-39", "Endereco": "Rua das Ninfas", "Redes Sociais": "@ecoloja"},
    3: {"Nome Fantasia": "Ecoloja", "Razao Social": "Ecoloja SA", "CNPJ": "22.206.183/0001-39", "Endereco": "Rua das Ninfas", "Redes Sociais": "@ecoloja"},
}


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






if __name__ == '__main__':
    app.run()