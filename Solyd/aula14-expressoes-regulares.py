import re
import requests

requisicao = requests.get('http://lacoxinha.com.br/contato')

string_teste = 'asas@awsas.com'

padrao = re.findall(r'[\w\.-]+@[\w-]+\.[\w\.-]+', requisicao.text)

if padrao:
    print(padrao)
else:
    print('Padrao não encontrado')