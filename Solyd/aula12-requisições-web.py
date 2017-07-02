import requests #Beautiful Soup 4 BS4 pip install bs4

cabecalho = {'User-agent': 'Windows 12',
             'Referer': 'https://google.com',
             'CF_IPcountry': 'us'}

meus_cookies = {'Ultima-visita ': '10-10-2020'}

dados = {'username': 'guigui',
         'password': 'guigui123'}

texto = None

try:
    requisicao = requests.post('http://putsreq.com/hary8S7lmAvPBnhWx7QS',
                               headers=cabecalho,
                               cookies=meus_cookies,
                               data=dados)
    texto = requisicao.text
except Exception as e:
    print('Requisição deu Erro: ', e)

print(texto)