class Caneta:
    def __init__(self, m, c, p):
        self._modelo = m
        self._cor = c
        self.ponta = p

    # def _get_modelo(self):
    #     print('Getter executado!')
    #     return self._modelo
    #
    # def _set_modelo(self, _modelo):
    #     print('Setter executado!')
    #     self._modelo = _modelo

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, _modelo):
        self._modelo = _modelo

    @property
    def sardinha(self):
        return self._cor

    @sardinha.setter
    def sardinha(self, _cor):
        self._cor = _cor

    def _del_modelo(self):
        print('Deletter executado!')
        raise AttributeError('Não pode deletar esse atributo')

    # modelo = property(_get_modelo, _set_modelo, _del_modelo)


c1 = Caneta('Bic', 'Azul', 0.5)
print(c1.modelo, c1.sardinha)
c1.modelo = 'Bic Moderna'
print(c1.modelo, c1.sardinha)
