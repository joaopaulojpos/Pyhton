import requests
import json

requisicao = requests.get('https://api.hgbrasil.com/weather/?format=json&woeid=457484')

tempo = json.loads(requisicao.text)

print('#### PREVISÃO DO TEMPO ####')
print('Cidade:', tempo['results']['city'], 'Dia:', tempo['results']['forecast'][0]['date'])
print('Min:', tempo['results']['forecast'][0]['min'], 'Max:', tempo['results']['forecast'][0]['max'])
print('Descrição:', tempo['results']['forecast'][0]['description'])