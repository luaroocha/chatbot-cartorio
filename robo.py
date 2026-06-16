import os
import sys

# O ChatterBot depende da ordem de iteração de sets/dicts para escolher a
# melhor resposta entre respostas com confiança igual. Sem PYTHONHASHSEED
# fixo, essa ordem muda a cada execução e o robô pode responder errado
# (confiança 0) para perguntas digitadas com acentuação normal.
if __name__ == "__main__" and os.environ.get("PYTHONHASHSEED") != "0":
    os.environ["PYTHONHASHSEED"] = "0"
    os.execv(sys.executable, [sys.executable] + sys.argv)

from chatterbot import ChatBot

NOME_ROBO = "RegisBot"
LIMIAR_ACEITACAO = 0.75

import time
time.clock = time.time

def iniciar():
    iniciado, robo = False, None

    try:
        robo = ChatBot(NOME_ROBO, read_only=True)

        iniciado = True
    except Exception as e:
        print(f"erro iniciando robô: {e}")

    return iniciado, robo

def get_resposta(robo, mensagem):
    resposta = robo.get_response(mensagem.lower())

    return resposta.confidence, resposta.text

if __name__ == "__main__":
    iniciado, robo = iniciar()
    if iniciado:
        while True:
            mensagem = input("👤: ")
            confianca, resposta = get_resposta(robo, mensagem)
            if confianca >= LIMIAR_ACEITACAO:
                print(f"🤖: {resposta} / confiança: {confianca}")
            else:
                #enviar pergunta não respondida para o log
                print("🤖: Desculpe, não entendi. Reformule, por favor!")
                print(f"🤖: Nível de confiança: {confianca}")