class Manimefo:
    def __init__(self, cor_de_pelo, genero, andar):
        self.cor_de_pelo = cor_de_pelo
        self.genero = genero
        self.num_de_patas = andar
    def falar(self):
        print('Olá sou um mamifero e eu sei falar')
    def andar(self):
        print('Estou andando sobre {} patas'.format(self.num_de_patas))
    def amamentar(self):
        if self.genero.lower()[0] == 'm':
            print('Machos não amamentam')
            return
        print('Amamentando meu filhote')


class Pessoa(Manimefo): #dizendo que Pessoa herda de mamifero
    def __init__(self, cor_de_pelo, genero, andar, cabelo):
        super(Pessoa, self).__init__(cor_de_pelo, genero, andar) #super () chamar o construtor da classe pai
        self.cabelo = cabelo
    def falar(self):
        super(Pessoa, self).falar()
        print('Olá soum uma pessoa e eu sei falar')

julia = Pessoa('preta', 'feminino', 2, 'Loiro')
julia.falar()