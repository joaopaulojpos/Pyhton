class Minha:

    def __init__(self, n, i):
        self.nome = n
        self.idade = i
        print('Construtor chamado com sucesso')

    def imprime(self, x):
        print('Olá meu nome é {} e eu tenho {}' .format(self.nome, self.idade))
        print(x)


pessoa = Minha('João Paulo', 23)

pessoa.imprime(5)