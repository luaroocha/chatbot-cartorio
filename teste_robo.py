import unittest
from robo import *


class TesteSaudacoes(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.iniciado, cls.robo = iniciar()

    def testar_01_iniciado(self):
        self.assertTrue(self.iniciado)
        self.assertIsNotNone(self.robo)

    def testar_02_oi_ola(self):
        saudacoes = ["oi", "olá", "oi, tudo bem?", "como vai?", "olá, como vai?", "ola como vai?", "ola"]
        for saudacao in saudacoes:
            print(f"testando: {saudacao}")

            confianca, resposta = get_resposta(self.robo, saudacao)
            self.assertGreaterEqual(confianca, LIMIAR_ACEITACAO)
            self.assertIn("Olá, sou o RegisBot", resposta)

    def testar_03_bom_dia(self):
        saudacoes = ["Bom dia", "Oi, bom dia", "Olá, bom dia", "bomdia"]
        for saudacao in saudacoes:
            print(f"testando: {saudacao}")

            confianca, resposta = get_resposta(self.robo, saudacao)
            self.assertEqual(confianca, 1.0)
            self.assertIn("Bom dia, sou o RegisBot", resposta)

    def testar_04_boa_tarde(self):
        saudacoes = ["Boa tarde", "Oi, boa tarde", "Olá, boa tarde"]
        for saudacao in saudacoes:
            print(f"testando: {saudacao}")

            confianca, resposta = get_resposta(self.robo, saudacao)
            self.assertEqual(confianca, 1.0)
            self.assertIn("Boa tarde, sou o RegisBot", resposta)

    def testar_05_boa_noite(self):
        saudacoes = ["Boa noite", "Oi, boa noite", "Olá, boa noite"]
        for saudacao in saudacoes:
            print(f"testando: {saudacao}")

            confianca, resposta = get_resposta(self.robo, saudacao)
            self.assertEqual(confianca, 1.0)
            self.assertIn("Boa noite, sou o RegisBot", resposta)


class TesteInformacoesBasicas(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.iniciado, cls.robo = iniciar()

    def testar_01_iniciado(self):
        self.assertTrue(self.iniciado)
        self.assertIsNotNone(self.robo)

    def testar_02_localizacao(self):
        perguntas = [
            "onde o cartorio está localizado?",
            "onde fica o cartorio?",
            "onde vocês funcionam?",
            "onde vocês estão localizados?",
            "onde fica?",
            "endereço"
        ]
        for pergunta in perguntas:
            print(f"testando: {pergunta}")

            confianca, resposta = get_resposta(self.robo, pergunta)
            self.assertEqual(confianca, 1.0)
            self.assertIn("O Cartório de Registro de Imóveis fica localizado na Praça Estevão Santos, 109, Centro, Vitoria da Conquista - BA", resposta)

    def testar_03_horario_funcionamento(self):
        perguntas = [
            "qual é o horário de funcionamento?",
            "que horas vocês ficam abertos?",
            "que horas o cartorio fica aberto?",
            "que horas o cartorio funciona?",
            "horario funcionamento",
            "horário de funcionamento",
            "funcionamento"
        ]
        for pergunta in perguntas:
            print(f"testando: {pergunta}")

            confianca, resposta = get_resposta(self.robo, pergunta)
            self.assertEqual(confianca, 1.0)
            self.assertIn("O Cartório de Registro de Imóveis funciona das 08:00 às 14:00, de segunda a sexta-feira", resposta)

    def testar_04_proprietario_imovel(self):
        perguntas = [
            "como saber quem é o proprietario do imovel?",
            "como descobrir quem é o proprietario do imovel?",
            "como buscar um imovel no cartorio?",
            "buscar imovel no cartorio"
        ]
        for pergunta in perguntas:
            print(f"testando: {pergunta}")

            confianca, resposta = get_resposta(self.robo, pergunta)
            self.assertEqual(confianca, 1.0)
            self.assertIn("Para saber quem é o proprietário de um imóvel", resposta)

    def testar_05_localizar_imovel(self):
        perguntas = [
            "como localizar um imovel no cartorio?",
            "localizar imovel no cartorio"
        ]
        for pergunta in perguntas:
            print(f"testando: {pergunta}")

            confianca, resposta = get_resposta(self.robo, pergunta)
            self.assertEqual(confianca, 1.0)
            self.assertIn("Para localizar um imóvel no Cartório de Registro de Imóveis", resposta)

    def testar_06_financiamento(self):
        perguntas = [
            "como formalizar o registro de um imóvel financiado?",
            "como registrar um imóvel financiado?",
            "imovel financiado registro",
            "registro de imovel financiado"
        ]
        for pergunta in perguntas:
            print(f"testando: {pergunta}")

            confianca, resposta = get_resposta(self.robo, pergunta)
            self.assertEqual(confianca, 1.0)
            self.assertIn("O financiamento é registrado na matrícula do imóvel mediante apresentação do contrato ao cartório.", resposta)

    def testar_07_certidao_matricula(self):
        perguntas = [
            "o que é uma certidão de matrícula atualizada?",
            "o que consta em uma certidão de matrícula atualizada?",
            "certidão matrícula atualizada",
            "certidão de matrícula atualizada",
            "certidão de matrícula atualizada do imóvel"
        ]
        for pergunta in perguntas:
            print(f"testando: {pergunta}")

            confianca, resposta = get_resposta(self.robo, pergunta)
            self.assertGreaterEqual(confianca, LIMIAR_ACEITACAO)
            self.assertIn("É um documento emitido pelo cartório que apresenta a situação atual do imóvel", resposta)

    def testar_08_averbacoes(self):
        perguntas = [
            "quais averbacoes posso fazer no cartorio?",
            "quais averbacoes posso fazer no cartorio de registro de imoveis?",
            "averbacoes cartorio",
            "averbacoes cartorio de registro de imoveis"
        ]
        for pergunta in perguntas:
            print(f"testando: {pergunta}")

            confianca, resposta = get_resposta(self.robo, pergunta)
            self.assertEqual(confianca, 1.0)
            self.assertIn("É possível averbar construções, demolições, casamentos, divórcios, alterações de nome e quitações de financiamento.", resposta)

    def testar_09_variabilidade_localizacao(self):
        pergunta = "Onde fica o cartório?"
        print(f"testando: {pergunta}")

        confianca, resposta = get_resposta(self.robo, pergunta)
        self.assertGreaterEqual(confianca, LIMIAR_ACEITACAO)
        self.assertIn("O Cartório de Registro de Imóveis fica localizado na Praça Estevão Santos, 109, Centro, Vitoria da Conquista - BA", resposta)

    def testar_10_variabilidade_horario_funcionamento(self):
        pergunta = "qual o horario de funcionamento?"
        print(f"testando: {pergunta}")

        confianca, resposta = get_resposta(self.robo, pergunta)
        self.assertGreaterEqual(confianca, LIMIAR_ACEITACAO)
        self.assertIn("O Cartório de Registro de Imóveis funciona das 08:00 às 14:00, de segunda a sexta-feira", resposta)

    def testar_11_variabilidade_proprietario_imovel(self):
        pergunta = "como sei quem é o dono do imovel?"
        print(f"testando: {pergunta}")

        confianca, resposta = get_resposta(self.robo, pergunta)
        self.assertGreaterEqual(confianca, LIMIAR_ACEITACAO)
        self.assertIn("Para saber quem é o proprietário de um imóvel", resposta)

    def testar_12_variabilidade_localizar_imovel(self):
        pergunta = "como localizar um imovel no cartorio"
        print(f"testando: {pergunta}")

        confianca, resposta = get_resposta(self.robo, pergunta)
        self.assertGreaterEqual(confianca, LIMIAR_ACEITACAO)
        self.assertIn("Para localizar um imóvel no Cartório de Registro de Imóveis", resposta)

    def testar_13_variabilidade_financiamento(self):
        pergunta = "Registro de imovel financiado"
        print(f"testando: {pergunta}")

        confianca, resposta = get_resposta(self.robo, pergunta)
        self.assertGreaterEqual(confianca, LIMIAR_ACEITACAO)
        self.assertIn("O financiamento é registrado na matrícula do imóvel mediante apresentação do contrato ao cartório.", resposta)

    def testar_14_variabilidade_certidao_matricula(self):
        pergunta = "certidão matrícula atualizada?"
        print(f"testando: {pergunta}")

        confianca, resposta = get_resposta(self.robo, pergunta)
        self.assertGreaterEqual(confianca, LIMIAR_ACEITACAO)
        self.assertIn("É um documento emitido pelo cartório que apresenta a situação atual do imóvel", resposta)

    def testar_15_variabilidade_averbacoes(self):
        pergunta = "Averbacoes cartorio"
        print(f"testando: {pergunta}")

        confianca, resposta = get_resposta(self.robo, pergunta)
        self.assertGreaterEqual(confianca, LIMIAR_ACEITACAO)
        self.assertIn("É possível averbar construções, demolições, casamentos, divórcios, alterações de nome e quitações de financiamento.", resposta)


if __name__ == "__main__":
    unittest.main()
