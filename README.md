# RegisBot - Chatbot do Cartório de Registro de Imóveis

Chatbot de atendimento construído com [ChatterBot](https://github.com/gunthercox/ChatterBot), treinado com perguntas e respostas sobre os serviços do cartório.

## Requisitos

- Python 3.x
- Node.js (apenas para a interface web de chat)

## Instalação

```bash
pip install -r requirements.txt
```

> Opcional: crie um ambiente virtual antes (`python -m venv venv` e ative com `.\venv\Scripts\Activate.ps1`) para isolar as dependências do Python global.

## Treinar o robô

Gera o arquivo `db.sqlite3` com o conhecimento treinado a partir dos arquivos em `conversas/`:

```bash
python treinamento.py
```

Execute novamente sempre que alterar os arquivos JSON em `conversas/`.

## Rodar o chatbot

### Console interativo
```bash
$env:PYTHONIOENCODING = "utf-8"
python robo.py
```

### API (Flask, porta 5000)
```bash
$env:PYTHONIOENCODING = "utf-8"
python servico.py
```

### Interface web de chat (porta 3000)
Com a API rodando em outro terminal:
```bash
cd chat
node index.js
```
Acesse `http://localhost:3000`.

## Rodar os testes

```bash
$env:PYTHONHASHSEED = "0"
$env:PYTHONIOENCODING = "utf-8"
python -m unittest teste_robo -v
```

> `PYTHONHASHSEED=0` é necessário para resultados consistentes (o ChatterBot pode retornar respostas diferentes entre execuções sem isso).
