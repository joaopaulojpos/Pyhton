class Complex():
    def __init__(self, real, imag):
        self._real = real
        self._imag = imag

    def get_real(self):
        return self._real

    def set_real(self, valor):
        self._real = valor

    real = property(
        fget=get_real,
        fset=set_real
    )


    def getImag(self):
        return self._imag


    def setImag(self, valor):
     self._imag = valor


    imag = property(
        fget=getImag,
        fset=setImag)

c = Complex(1, 0)
c.set_real(2)
print(c.get_real())