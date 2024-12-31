# TSI

Este repositório contém um script Python para gerar embeddings a partir de um texto utilizando a API do Ollama. O código realiza uma requisição POST para o endpoint local do Ollama e retorna os embeddings baseados no modelo all-minilm.

# Pré-requisitos
Python 3.x e biblioteca requests

# Instale a dependência com:
pip install requests

# Dependências Adicionais
Certifique-se de que o Ollama está configurado e rodando localmente no endpoint http://localhost:11434/v1/embeddings.

# Execute o script com:
python gerar_embeddings.py

O script fará uma requisição POST para o servidor Ollama local e exibirá os embeddings gerados ou um erro em caso de falha.
