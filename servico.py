import os
import sys

# Mesma ressalva do robo.py: o serviço precisa do PYTHONHASHSEED fixo para
# o ChatterBot escolher consistentemente a resposta correta.
if __name__ == "__main__" and os.environ.get("PYTHONHASHSEED") != "0":
    os.environ["PYTHONHASHSEED"] = "0"
    os.execv(sys.executable, [sys.executable] + sys.argv)

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
def responder(mensagem):
    confianca, texto = get_resposta(robo, mensagem)
    resposta = {
        "resposta": texto,
        "confianca": confianca
    }

    return Response(json.dumps(resposta), status=200, mimetype="application/json")


if __name__ == "__main__":
    servico.run(host="0.0.0.0", port=5000)