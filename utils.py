import json

def load_data(caminho):
    caminho_completo = f'static/data/{caminho}'
    with open(caminho_completo, 'r', encoding='utf-8') as arquivo:
        return json.load(arquivo)

def add_data(caminho, nova_anotacao):
    dados = load_data(caminho)
    dados.append(nova_anotacao)

    caminho_completo = f'static/data/{caminho}'
    with open(caminho_completo, 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=2)

def load_template(arquivo):
    caminho_completo = f'static/templates/{arquivo}'
    with open(caminho_completo, 'r') as arquivo:
            return arquivo.read()
