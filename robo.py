from chatterbot import ChatBot
from normalizador import normalizar

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
    resposta = robo.get_response(normalizar(mensagem))

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
                print("🤖: Desculpe, não entendi. Reformule, por favor!")
                print(f"🤖: Nível de confiança: {confianca}")
