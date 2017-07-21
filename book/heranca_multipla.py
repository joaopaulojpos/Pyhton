class Pai:
    altura = 'Entre 180 e 190 centimetros'
    cor_dos_olhos = 'Castanhos'

class Mae:
    def corPreferida(self):
        print('A minha cor preferida é branco !')

class Filho(Pai, Mae):
    def informacao(self):
        print('Nome: Nelson Silva')
        print('Idade: 21')
        print('Altura:', self.altura)
        print('Cor dos olhos: ', self.cor_dos_olhos)

pessoa = Filho()

pessoa.informacao()
pessoa.corPreferida()