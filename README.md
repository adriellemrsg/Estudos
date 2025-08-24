# 📊 Consumo de Dados do IBGE - SIDRA (Tabela 8880)

Este script em Python consome dados da API do **SIDRA/IBGE** (Tabela 8880)  
e armazena os resultados em formato **JSON**, criando automaticamente o diretório de destino.

---

## 🚀 Fluxo do Script

1. **Requisição à API**  
   - URL consultada:  
     ```
     https://apisidra.ibge.gov.br/values/t/8880/n1/all/p/all?formato=json
     ```
   - Os dados retornam em formato JSON.

2. **Criação do diretório de destino**  
   - O script cria (se não existir) a pasta:
     ```
     ../Data/Landing/ibge_sidra_8880
     ```

3. **Armazenamento dos dados**  
   - O arquivo é salvo como:
     ```
     ibge_sidra_8880.json
     ```

---

## 📂 Estrutura esperada

```
Data/
└── Landing/
    └── ibge_sidra_8880/
        └── ibge_sidra_8880.json
```

---

## 🔧 Pré-requisitos

- Python 3.8+
- Bibliotecas:
  - `requests`
  - `os` (nativa do Python)
  - `json` (nativa do Python)

Instalação do `requests`:
```bash
pip install requests
```

---

## ▶️ Execução

```bash
python script_ibge_sidra_8880.py
```

---

## 📌 Observações

- O parâmetro `response.raise_for_status()` garante que o script pare caso a requisição falhe.
- Os dados são salvos em UTF-8, preservando acentos.
- O JSON é formatado com indentação para facilitar leitura e versionamento.

---
