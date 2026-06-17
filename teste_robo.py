import os
import sys

if os.environ.get("PYTHONHASHSEED") != "0":
    os.environ["PYTHONHASHSEED"] = "0"
    os.execv(sys.executable, [sys.executable] + sys.argv)

import unittest
from robo import *

W = 70


def _log(frase, confianca, resposta):
    resp_curta = (resposta[:52] + "...") if len(resposta) > 55 else resposta
    print(f"       Entrada   : {frase}", flush=True)
    print(f"       Confianca : {confianca:.2f}  |  Resposta: {resp_curta}", flush=True)


class ResultadoFormatado(unittest.TextTestResult):

    def __init__(self, stream, descriptions, verbosity):
        super().__init__(stream, descriptions, verbosity)
        self._classe_atual = None
        self._numero = 0

    def startTestRun(self):
        self.stream.write("\n" + "=" * W + "\n")
        self.stream.write("  RegisBot - Testes Automatizados\n")
        self.stream.write("  Cartorio de Registro de Imoveis\n")
        self.stream.write("=" * W + "\n")
        self.stream.flush()

    def startTest(self, test):
        super().startTest(test)
        self._numero += 1
        nome_classe = type(test).__name__

        if self._classe_atual != nome_classe:
            self._classe_atual = nome_classe
            self.stream.write(f"\n{'-' * W}\n")
            self.stream.write(f"  {nome_classe}\n")
            self.stream.write(f"{'-' * W}\n")

        self.stream.write(f"\n  [{self._numero:02d}] {test._testMethodName}\n")
        self.stream.flush()

    def addSuccess(self, test):
        super().addSuccess(test)
        self.stream.write(f"\n       Status    : APROVADO\n")
        self.stream.flush()

    def addFailure(self, test, err):
        super().addFailure(test, err)
        detalhe = str(err[1]).strip().split("\n")[-1]
        self.stream.write(f"\n       Status    : REPROVADO  ({detalhe})\n")
        self.stream.flush()

    def addError(self, test, err):
        super().addError(test, err)
        self.stream.write(f"\n       Status    : ERRO  ({str(err[1])})\n")
        self.stream.flush()

    def stopTestRun(self):
        total     = self.testsRun
        falhas    = len(self.failures) + len(self.errors)
        aprovados = total - falhas

        self.stream.write(f"\n{'=' * W}\n")
        self.stream.write(f"  RESULTADO FINAL\n")
        self.stream.write(f"{'=' * W}\n")
        self.stream.write(f"  Total executados  :  {total}\n")
        self.stream.write(f"  Aprovados         :  {aprovados}\n")
        self.stream.write(f"  Reprovados        :  {falhas}\n")
        self.stream.write(f"{'-' * W}\n")
        if falhas == 0:
            self.stream.write(f"  Resultado  :  TODOS OS TESTES PASSARAM\n")
        else:
            self.stream.write(f"  Resultado  :  {falhas} TESTE(S) REPROVADO(S)\n")
        self.stream.write(f"{'=' * W}\n\n")
        self.stream.flush()


class RunnerFormatado(unittest.TextTestRunner):
    resultclass = ResultadoFormatado

    def __init__(self):
        super().__init__(verbosity=0, stream=sys.stdout, buffer=False)

    def run(self, test):
        result = self._makeResult()
        result.startTestRun()
        test(result)
        result.stopTestRun()
        return result


class TesteSaudacoes(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.iniciado, cls.robo = iniciar()

    def testar_01_iniciado(self):
        self.assertTrue(self.iniciado)
        self.assertIsNotNone(self.robo)
        print(f"       Robo     : {NOME_ROBO}", flush=True)
        print(f"       Iniciado : {self.iniciado}", flush=True)

    def testar_02_oi_ola(self):
        saudacoes = ["oi", "oi, tudo bem?", "como vai?", "olá, como vai?", "ola como vai?", "ola"]
        for saudacao in saudacoes:
            confianca, resposta = get_resposta(self.robo, saudacao)
            _log(saudacao, confianca, resposta)
            self.assertGreaterEqual(confianca, LIMIAR_ACEITACAO)
            self.assertIn("Olá, sou o RegisBot", resposta)

    def testar_03_bom_dia(self):
        saudacoes = ["Bom dia", "Oi, bom dia", "Olá, bom dia", "bomdia"]
        for saudacao in saudacoes:
            confianca, resposta = get_resposta(self.robo, saudacao)
            _log(saudacao, confianca, resposta)
            self.assertEqual(confianca, 1.0)
            self.assertIn("Bom dia, sou o RegisBot", resposta)

    def testar_04_boa_tarde(self):
        saudacoes = ["Boa tarde", "Oi, boa tarde", "Olá, boa tarde"]
        for saudacao in saudacoes:
            confianca, resposta = get_resposta(self.robo, saudacao)
            _log(saudacao, confianca, resposta)
            self.assertEqual(confianca, 1.0)
            self.assertIn("Boa tarde, sou o RegisBot", resposta)

    def testar_05_boa_noite(self):
        saudacoes = ["Boa noite", "Oi, boa noite", "Olá, boa noite"]
        for saudacao in saudacoes:
            confianca, resposta = get_resposta(self.robo, saudacao)
            _log(saudacao, confianca, resposta)
            self.assertEqual(confianca, 1.0)
            self.assertIn("Boa noite, sou o RegisBot", resposta)


class TesteInformacoesBasicas(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.iniciado, cls.robo = iniciar()

    def testar_01_iniciado(self):
        self.assertTrue(self.iniciado)
        self.assertIsNotNone(self.robo)
        print(f"       Robo     : {NOME_ROBO}", flush=True)
        print(f"       Iniciado : {self.iniciado}", flush=True)

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
            confianca, resposta = get_resposta(self.robo, pergunta)
            _log(pergunta, confianca, resposta)
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
            confianca, resposta = get_resposta(self.robo, pergunta)
            _log(pergunta, confianca, resposta)
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
            confianca, resposta = get_resposta(self.robo, pergunta)
            _log(pergunta, confianca, resposta)
            self.assertEqual(confianca, 1.0)
            self.assertIn("Para saber quem é o proprietário de um imóvel", resposta)

    def testar_05_localizar_imovel(self):
        perguntas = [
            "como localizar um imovel no cartorio?",
            "localizar imovel no cartorio"
        ]
        for pergunta in perguntas:
            confianca, resposta = get_resposta(self.robo, pergunta)
            _log(pergunta, confianca, resposta)
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
            confianca, resposta = get_resposta(self.robo, pergunta)
            _log(pergunta, confianca, resposta)
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
            confianca, resposta = get_resposta(self.robo, pergunta)
            _log(pergunta, confianca, resposta)
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
            confianca, resposta = get_resposta(self.robo, pergunta)
            _log(pergunta, confianca, resposta)
            self.assertEqual(confianca, 1.0)
            self.assertIn("É possível averbar construções, demolições, casamentos, divórcios, alterações de nome e quitações de financiamento.", resposta)

    def testar_09_variabilidade_localizacao(self):
        pergunta = "Onde fica o cartório?"
        confianca, resposta = get_resposta(self.robo, pergunta)
        _log(pergunta, confianca, resposta)
        self.assertGreaterEqual(confianca, LIMIAR_ACEITACAO)
        self.assertIn("O Cartório de Registro de Imóveis fica localizado na Praça Estevão Santos, 109, Centro, Vitoria da Conquista - BA", resposta)

    def testar_10_variabilidade_horario_funcionamento(self):
        pergunta = "qual o horario de funcionamento?"
        confianca, resposta = get_resposta(self.robo, pergunta)
        _log(pergunta, confianca, resposta)
        self.assertGreaterEqual(confianca, LIMIAR_ACEITACAO)
        self.assertIn("O Cartório de Registro de Imóveis funciona das 08:00 às 14:00, de segunda a sexta-feira", resposta)

    def testar_11_variabilidade_proprietario_imovel(self):
        pergunta = "como sei quem é o dono do imovel?"
        confianca, resposta = get_resposta(self.robo, pergunta)
        _log(pergunta, confianca, resposta)
        self.assertGreaterEqual(confianca, LIMIAR_ACEITACAO)
        self.assertIn("Para saber quem é o proprietário de um imóvel", resposta)

    def testar_12_variabilidade_localizar_imovel(self):
        pergunta = "como localizar um imovel no cartorio"
        confianca, resposta = get_resposta(self.robo, pergunta)
        _log(pergunta, confianca, resposta)
        self.assertGreaterEqual(confianca, LIMIAR_ACEITACAO)
        self.assertIn("Para localizar um imóvel no Cartório de Registro de Imóveis", resposta)

    def testar_13_variabilidade_financiamento(self):
        pergunta = "Registro de imovel financiado"
        confianca, resposta = get_resposta(self.robo, pergunta)
        _log(pergunta, confianca, resposta)
        self.assertGreaterEqual(confianca, LIMIAR_ACEITACAO)
        self.assertIn("O financiamento é registrado na matrícula do imóvel mediante apresentação do contrato ao cartório.", resposta)

    def testar_14_variabilidade_certidao_matricula(self):
        pergunta = "certidão matrícula atualizada?"
        confianca, resposta = get_resposta(self.robo, pergunta)
        _log(pergunta, confianca, resposta)
        self.assertGreaterEqual(confianca, LIMIAR_ACEITACAO)
        self.assertIn("É um documento emitido pelo cartório que apresenta a situação atual do imóvel", resposta)

    def testar_15_variabilidade_averbacoes(self):
        pergunta = "Averbacoes cartorio"
        confianca, resposta = get_resposta(self.robo, pergunta)
        _log(pergunta, confianca, resposta)
        self.assertGreaterEqual(confianca, LIMIAR_ACEITACAO)
        self.assertIn("É possível averbar construções, demolições, casamentos, divórcios, alterações de nome e quitações de financiamento.", resposta)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(TesteSaudacoes))
    suite.addTests(loader.loadTestsFromTestCase(TesteInformacoesBasicas))
    RunnerFormatado().run(suite)
