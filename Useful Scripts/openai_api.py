import openai

# Configure sua chave de API
openai.api_key = 'sua_chave_de_api_aqui'

# Exemplo de solicitação à API
response = openai.Completion.create(
  engine="text-davinci-002",
  prompt="Translate the following English text to French: '{}'",
  max_tokens=60
)

# Imprima a resposta da API
print(response['choices'][0]['text'])
