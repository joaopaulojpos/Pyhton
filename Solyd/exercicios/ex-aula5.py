'''
EXERCICIO: Faça um programa que leia a quantidade de pessoas que
forao convidadas para uma festa.
Após isso o programa irá perguntar o nome de todas as pessoas e
colocar numa lista de convidados
Após isso irá imprimir todos os nomes da lista
'''

print('Programa de controle de Festas 1.0')
print('##################################')
numero_de_convidados = int(input('Coloque o numero de convidados: '))
lista_de_convidados = []

i = 1
while i <= numero_de_convidados:
    nome_do_convidado = input('Coloque o nome do convidado #' + str(i) +': ')
    lista_de_convidados.append(nome_do_convidado)
    i += 1

print('Serão', numero_de_convidados, 'Convidados')

print('\nLISTA DE CONVIDADOS')

for convidado in lista_de_convidados:
    print(convidado)