class Calculadora():
    #H
    def __init__(self):
        self.resultado = 0

    def obtener_resultado(self):
        return self.resultado

    def suma(self, num1, num2):
        if type(num1) is str or type(num2) is str:
            self.resultado = 'datos incorrectos'
        else:
            self.resultado = num1 + num2

    def resta(self, num1, num2):
        if type(num1) is str or type(num2) is str:
            self.resultado = 'datos incorrectos'
        else:
            self.resultado = num1 - num2

    def multiplicacion(self, num1, num2):
        if type(num1) is str or type(num2) is str:
            self.resultado = 'datos incorrectos'
        else:
            self.resultado = num1 * num2

    def dividir(self, num1, num2):
        if type(num1) is str or type(num2) is str:
            self.resultado = 'datos incorrectos'
        elif num2 == 0:
            self.resultado = 'datos invalido en divisor'
        else:
            self.resultado = num1 / num2

    def potencia(self, num1, num2):
        if type(num1) is str or type(num2) is str:
            self.resultado = 'datos incorrectos'
        else:
            self.resultado = num1 ** num2

    def raiz(self, num1, num2):
        if type(num1) is str or type(num2) is str:
            self.resultado = 'datos incorrectos'
        elif num1 < 0:
            self.resultado = 'No se puede sacar raiz a un num negativo'
        else:
            self.resultado = num1 ** (1.0 / num2)

