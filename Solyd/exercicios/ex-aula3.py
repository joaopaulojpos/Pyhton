'''
EXERCICIO
Faça um programa que pergunte a idade, o peso e a altura de
uma pessoa e decide se ela está apta a ser do Exercito
Para entrar no exercito é preciso ter mais de 18 anos
pesar mais ou igual a 60 kilos
e medir mais ou igual 1,70 metros
'''

idade = int(input('Digite sua idade: '))
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

if idade > 18 and peso >= 60 and altura >= 1.70:
    print('Você esta apto a entrar no Exercito')
else:
    print('Você não esta apto a entrar no Exercito')