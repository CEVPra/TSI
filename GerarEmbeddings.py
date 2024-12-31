import requests
import json

OLLAMA_URL = "http://localhost:11434/v1/embeddings"

text = "como calcular a raiz quadrada de 9?"

model = "all-minilm"

data = {
    "model": model,
    "input": text
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(OLLAMA_URL, headers=headers, json=data)

if response.status_code == 200:
    embeddings = response.json()
    print(f"Embeddings gerados com sucesso: {embeddings}")
else:
    print(f"Erro ao gerar embeddings: {response.status_code}, {response.text}")