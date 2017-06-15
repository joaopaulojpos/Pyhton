minha_string = "Olá Mundo ! 'João Paulo' "
minha_string = '''Esta é uma string que contém\n linhas puladas, como podem ver\nAdeus!'''

curso = 'Python 3 '
nome = 'João Paulo'

msg_final = 'Novo Curso de ' + curso + 'por ' + nome #1 forma
msg_final = 'Novo Curso de {} por {} '.format(curso, nome) #forma mais indicada

print(minha_string)
print(msg_final)