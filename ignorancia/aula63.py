class ObjetoGrafico:

    def __init__(self, cor):
        self.cor = cor

    def area(self):
        pass

    def perimetro(self):
        pass

    def info(self):
        print('{} metros2 serão preenchidos com a cor {}'.format(self.area(), self.cor))


class Cachorro:
    nome = 'Rex'
    cor = 'marrom'

dog = Cachorro()
print(dog.nome)
print(Cachorro.nome)