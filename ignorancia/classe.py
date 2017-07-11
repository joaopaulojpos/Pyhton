class Classe:
    def __init__(self):
        self.x = 0
        self.y = 0

class PessoaS2Animais:
    def __init__(self, nome, peso, cao):
        self.nome = nome
        self.peso = peso
        self.cao = cao

    def treinar(self):
        self.cao.daApatinha()
        self.cao.latir()

class Cachorro:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor
    def daApatinha(self):
        print('{} extendeu a patinha'.format(self.nome))
    def latir(self):
        print('AUAUAUUAAUA!')

rex = Cachorro('Rex', 'marrom')
pedro = PessoaS2Animais('João', 75, rex)

print(pedro.cao.cor)
print(pedro.treinar())

def MudaNome(pessoa):
    pessoa.nome = 'Lucas'

MudaNome(pedro)
print(pedro.nome)