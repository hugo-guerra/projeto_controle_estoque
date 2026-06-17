import json
import os

estoque = 'dados/estoque.json'

def carregar_dados():

    if os.path.exists(estoque):
        with open(estoque, 'r') as arquivo:
            dados = json.load(arquivo)
        return dados
    
    else: return {}

def salvar_dados(dados):
    with open(estoque, 'w') as arquivo:
        json.dump(dados, arquivo)