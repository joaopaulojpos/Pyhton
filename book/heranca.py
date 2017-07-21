class Pessoa:

    def __init__(self, nome, idade, sexo):
        self._nome = nome
        self._idade = idade
        self._sexo = sexo

    def fazer_aniversario(self):
        self._idade += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, _nome):
        self._nome = _nome

    @property
    def idade(self):
         return self._idade

    @idade.setter
    def idade(self, _idade):
         self._idade = _idade

    @property
    def sexo(self):
        return self._sexo

    @sexo.setter
    def sexo(self, _sexo):
        self._sexo = _sexo

class Professor(Pessoa):

    def __init__(self, nome, idade, sexo, especialidade, salario):
        super(Professor, self).__init__(nome, idade, sexo)
        self._especialidade = especialidade
        self._salario = salario

    def receber_aumento(self, aum):
         self._salario += aum

    def _get_especialidade(self):
         return self._especialidade

    def _set_especialidade(self, _especialidade):
        self._especialidade = _especialidade

    def _get_salario(self):
        return self._salario

    def _set_salario(self, _salario):
        self._salario = _salario

    especialidade = property(_get_especialidade, _set_especialidade)
    salario = property(_get_salario, _get_salario)

p1 = Pessoa('João', 23, 'M')
p2 = Professor('José', 45, 'M', 'Programação', 2500.75)

print(p1.nome, p1.idade, p1.sexo)
print(p2.nome, p2.idade, p2. sexo, p2.especialidade, p2.salario)
p2.fazer_aniversario()
p2.nome = 'Juca'
p2.receber_aumento(550.20)
print(p2.nome, p2.idade, p2. sexo, p2.especialidade, p2.salario)