import json
import flask

app = flask.Flask(__name__)

lojas = {
    1: {"Nome Fantasia": "Ecoloja", "Razao Social": "Ecoloja SA", "CNPJ": "22.206.183/0001-39", "Endereco": "Rua das Ninfas, 281 - Soledade, Recife", "Redes Sociais": "@ecoloja"},
    2: {"Nome Fantasia": "Sabor Natural", "Razao Social": "Sabor Natural LTDA", "CNPJ": "34.937.499/0001-80", "Endereco": "Rua Joaquim Tenório, 324 - Cavaleiro, Jaboatão dos Guararapes", "Redes Sociais": "@sabor.natural"},
    3: {"Nome Fantasia": "Verde Vivo", "Razao Social": "Verde Vivo SA", "CNPJ": "67.151.470/0001-27", "Endereco": "Rua Deolindo Taváres, 263 - Imbiribeira, Recife", "Redes Sociais": "@verdevivo"},
    4: {"Nome Fantasia": "Essência Orgânica", "Razao Social": "Essência Orgânica SS", "CNPJ": "24.039.585/0001-11", "Endereco": "Rua José Osório, 580 - Madalena, Recife", "Redes Sociais": "@essenciaorganica"},
    5: {"Nome Fantasia": "Raízes Sustentáveis", "Razao Social": "Raízes Sustentáveis LTDA", "CNPJ": "90.741.494/0001-58", "Endereco": "Avenida Barão de Bonito, 1110 - Várzea, Recife", "Redes Sociais": "@raizessustentaveis"},
    6: {"Nome Fantasia": "Naturallis", "Razao Social": "Naturallis SA", "CNPJ": "16.829.653/0001-18", "Endereco": "Rua São Miguel, 77 - Afogados, Recife", "Redes Sociais": "@naturallis"},
    7: {"Nome Fantasia": "BioMarket", "Razao Social": "BioMarket SA", "CNPJ": "66.729.434/0001-35", "Endereco": "Rua Valdemar Falcão, 610 - Engenho do Meio, Recife", "Redes Sociais": "@biomarket"},
    8: {"Nome Fantasia": "EcoVida", "Razao Social": "EcoVida SS", "CNPJ": "58.392.661/0001-90", "Endereco": "Rua de São Bento, 239 - Varadouro, Olinda", "Redes Sociais": "@ecovida"},
    9: {"Nome Fantasia": "Essência da Terra", "Razao Social": "Essência da Terra SA", "CNPJ": "58.669.542/0001-31", "Endereco": "Avenida Liberdade, 950 - Sancho, Recife", "Redes Sociais": "@essenciadaterra"},
    10: {"Nome Fantasia": "Orgânica Mente", "Razao Social": "Orgânica Mente LTDA", "CNPJ": "02.920.063/0001-91", "Endereco": "Rua das Águas Verdes, 230 - São José, Recife", "Redes Sociais": "@organicamente"},
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