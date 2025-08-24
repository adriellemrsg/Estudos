"""
Script para consumo da API SIDRA/IBGE (tabela 8880) e salvamento dos dados em JSON.

Fluxo:
1. Faz requisição para a API do IBGE (SIDRA).
2. Cria diretório de destino (se não existir).
3. Salva os dados brutos (JSON) no diretório.
"""

import requests
import os
import json

# URL da API SIDRA/IBGE (tabela 8880)
url = "https://apisidra.ibge.gov.br/values/t/8880/n1/all/p/all?formato=json"

# 1. Requisição para a API
response = requests.get(url)
response.raise_for_status()  # Interrompe caso a requisição falhe
dados = response.json()

# 2. Diretório de destino
caminho = "../Data/Landing/ibge_sidra_8880"
os.makedirs(caminho, exist_ok=True)  # Cria diretório, se não existir
print(f"Pasta '{caminho}' criada com sucesso!")

# 3. Caminho do arquivo de saída
caminho_arquivo = os.path.join(caminho, "ibge_sidra_8880.json")

# 4. Salvando dados em arquivo JSON
with open(caminho_arquivo, "w", encoding="utf-8") as f:
    json.dump(dados, f, ensure_ascii=False, indent=4)

print(f"Arquivo salvo em: {caminho_arquivo}")
