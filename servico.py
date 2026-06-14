from robo import *
from flask import Flask, Response
import json

from treinamento import NOME_ROBO

iniciado, robo = iniciar()
servico = Flask(NOME_ROBO)

@servico.get("/")
def get_info():
    return json.dumps({
        "nome": NOME_ROBO,
        "descricao": "Robô de atendimento do Cartório de Registro de Imóveis"
    })
  
@servico.get("/resposta/<string:mensagem>")
def get_resposta(mensagem):
    resposta = robo.get_response(mensagem)
    resposta = {
        "resposta": resposta.text,
        "confianca": resposta.confidence
    }
    
    return Response (json.dumps(resposta), status=200, mimetype="application/json")


if __name__ == "__main__":
    servico.run(host="0.0.0.0", port=5000)