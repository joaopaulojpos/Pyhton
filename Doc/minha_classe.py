class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
print(x.r, x.i)

x.contador = 1
while x.contador < 10:
    x.contador = x.contador * 2
print(x.contador)
del x.contador