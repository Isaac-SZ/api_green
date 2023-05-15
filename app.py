import json
import flask

app = flask.Flask(__name__)

lojas = {
    1: {"Nome": "Ecoloja", "Endereco": "Rua das Ninfas", "Telefone": "99999-9999"},
    2: {"Nome": "Organics", "Endereco": "Rua da Aurora", "Telefone": "99999-9992"},
    3: {"Nome": "Feira do Ze", "Endereco": "Rua do zezinho", "Telefone": "99999-9993"},
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