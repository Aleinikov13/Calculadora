class Calculadora():
	def __init__(self):
		self.resultado = 0

	def obtener_resultado(self):
		return self.resultado

	def suma(self, num1, num2):
		self.resultado = num1 + num2

	def resta(self, num1, num2):
		self.resultado = num1 - num2

	def multiplicacion(self, num1, num2):
		self.resultado = num1 * num2

	def dividir(self, num1, num2):
		self.resultado = num1 / num2

	def potencia(self, num1, num2):
		self.resultado = num1 ** num2

	def raiz(self, num1, num2):
		self.resultado = num1 ** (1.0 / num2)
