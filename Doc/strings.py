#print('Ovos de Spam') #abordagem Simples
#print('doesn \'t') #use \' para colocar um scape da citação única
#print("não") #ou use também aspas duplas
#print('"Sim", ele disse')
#print('"Isn \' t", ela disse')

#s = 'Primeira Linha. \n Segunda Linha. ' # \n pula uma linha
#print(s)

#print('C: \ some \name')
#print(r'C: \ some \name') #utiliza o R para não interpretar os caracteres especias
'''
print(""" \
Usage: thingy [OPTIONS]
    -h      Exibir esta mensagem de uso
    -H      Hostname para se conectar
""")
'''

#print(3 * 'un' + 'io') # o * significa que o un vai se repetir 3 vezes
#print('Py' 'thon') #duas strings ao lado, são automaticamentes concatenadas
#prefixo = 'Py'
#print(prefixo + 'thon')

#texto = ('Coloque várias Strings entre parênteses'
#        'para que elas se juntem.')
#print(texto)

palavra = 'Python'
#print(palavra[0]) #exibi o caractere na posiçao indicada []
#print(palavra[5])

#print(palavra[-1]) #Pega o indice da direita para esquerda
#print(palavra[-2])

#------------- Fatiando a String ----------------#

print(palavra[0:2]) #[0(inclui):2(exclui)] inicio e fim do fatiamento
print(palavra[2:5])
print(palavra[:2]) #o zero esta implicito, anda ate a posição excluida
print(palavra[4:]) #caractere incluido pegando pelo final
print(palavra[-2:])
print('J' + palavra[1:]) #concatenando as Strings
print(palavra[:2] + 'py')

#---------- Retornado o comprimento da String --------------#
print(len(palavra))