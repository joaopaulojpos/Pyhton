import oauth2
import json
import pprint #para imprimir bonitinho
import urllib.parse #converter os caracteres especiais para ser aceito

consumer_key = 'NnNRzB3A22aUmFvCGPBU5f4Ow'
consumer_secret = 'iKGsqbBQnpxgNzILQVq1pTcDCS20gH6S8AV3eSx6hlT1mG5dYZ'


token_key = '197943708-qgmdAuqOdFE2ai2vkBdH6BlzogAJXuyCcqYT7Z27'
token_secret = 'OotxqoxNWKEv0iOh8F8fsgstHzt9DJe8Fd3yMijQyAMuE'

consumer = oauth2.Consumer(consumer_key, consumer_secret)
token = oauth2.Token(token_key, token_secret)
cliente = oauth2.Client(consumer, token)

query = input('Pesquisa: ')
query_codificada = urllib.parse.quote(query, safe='')
requisicao = cliente.request('https://api.twitter.com/1.1/search/tweets.json?q=' + query_codificada + '&lang=pt')

decodificar = requisicao[1].decode() #decodificando a requisicao

objeto = json.loads(decodificar) #Transformando o JSON em um objeto do Python

twittes = objeto['statuses']

for twit in twittes:
    print(twit['user']['screen_name'])
    print(twit['text'])
    print()

# pprint.pprint(objeto['statuses'][0]['user']['screen_name'])
# pprint.pprint(objeto['statuses'][0]['text'])