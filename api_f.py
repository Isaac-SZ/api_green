import json
import flask

app = flask.Flask(__name__)

lojas = {
    1: {"Nome": "Ecoloja", "Endereco": "Rua das Ninfas", "Telefone": "99999-9999"},
    2: {"Nome": "Organics", "Endereco": "Rua da Aurora", "Telefone": "99999-9992"},
    3: {"Nome": "Feira do Zé", "Endereco": "Rua do zezinho", "Telefone": "99999-9993"},
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




if __name__ == '__main__':
    app.run()