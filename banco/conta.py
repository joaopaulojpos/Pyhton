class Conta:

    def __init__(self, cliente, saldo, limite):
        self.cliente = cliente
        self.saldo = saldo
        self.limite = 0 - limite

    def sacar(self, valor):
        if self.saldo - valor < self.limite:
            print('Saldo insuficiente')
        else:
            self.saldo -= valor
            print('Foi sacado: ', valor)

    def consultar(self):
        return self.saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print('Foi depositado: ', valor)
        else:
            print('Erro no deposito')