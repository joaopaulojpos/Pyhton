class Pessoa:
    def __init__(self, nome, emprego, idade):
        self.nome = nome
        self.emprego = emprego
        self.idade = idade

    def ola (self):
        print('Olá meu nome é {} tenho {} anos e sou {}'.format(self.nome, self.idade, self.emprego))

lucas = Pessoa('Lucas', 'Advogado', 20)
print(lucas.__dict__)