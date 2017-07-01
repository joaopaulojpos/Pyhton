class Veiculo:

    def __init__(self, cor, rodas, marca, tanque):
        self.cor = cor
        self.marca = marca
        self.tanque = tanque

    def abastecer(self, litros):
        self.tanque += litros