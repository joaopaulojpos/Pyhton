import requests
import json

def requisicao(cep):

    try:
        req = requests.get('https://viacep.com.br/ws/' + cep + '/json/')
        dicionario = json.loads(req.text)
        return dicionario
    except:
        print('Erro na conexão')
        return None

def printar_detalhes(numero_cep):
    print('Cidade: ', numero_cep['localidade'])
    print('Rua: ', numero_cep['logradouro'])
    print('Bairro: ', numero_cep['bairro'])
    print('Estado: ', numero_cep['uf'])
    print('')

sair = False
while not sair:
    op = input('Digite um CEP com 8 digitos ou digite SAIR para fechar: ')

    if op == 'SAIR':
        sair = True
        print('Saindo...')
    else:
        numero_cep = requisicao(op)
        printar_detalhes(numero_cep)


