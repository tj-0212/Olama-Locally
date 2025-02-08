import ollama

# to pull a model use ollama.pull('model-name)

model_name = 'llama3.2:latest'

#to generate data
result = ollama.generate(model=model_name, prompt="Give me a joke on ollama")
print(result['response'])

#for chatting

response = ollama.chat(model=model_name, messages=[{
    'role':'user',
    'content':'give me a joke on ollama',
    },
    ])
print(response['message']['content'])


#creating yout own model
# modelfile = '''
# FROM model-name
# SYSTEM you are a chatbot for film
# '''
# ollama.create(model='my-bot-name',modelfile = modelfile)

#for listing models
print(ollama.list())

#ollama using rest api
# from ollama import Client
# client = Client(host = 'https://localhost:xxxxx')
# response = ollama.chat(model=model_name, messages=[{
#     'role':'user',
#     'content':'give me a joke on ollama',
#     },
#     ])
# print(response['message']['content'])


