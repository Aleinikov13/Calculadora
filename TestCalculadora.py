import unittest

from calculadora import Calculadora

class CalculadoraTest(unittest.TestCase):

	def setUp(self):
		self.calc = Calculadora()


	#Suma
	def test_valor_de_inicio_es_igual_a_cero(self):
		self.assertEquals(self.calc.obtener_resultado(), 0)

	def test_sumar_2_mas_2_igual_4(self):
		self.calc.suma(2, 2)
		self.assertEquals(self.calc.obtener_resultado(),4)

	def test_sumar_3_mas_3_igual_6(self):
		self.calc.suma(3, 3)
		self.assertEquals(self.calc.obtener_resultado(),6)

	def test_sumar_menos1_mas_2_igual_1(self):
		self.calc.suma(-1, 2)
		self.assertEquals(self.calc.obtener_resultado(),1)

	def test_sumas_l_mas_2_igual_dato_invalido(self):
		self.calc.suma('L', 2)
		self.assertEquals(self.calc.obtener_resultado(),'datos incorrectos')	

	#Resta
	def test_restar_3_menos_2_igual_1(self):
		self.calc.resta(3, 2)
		self.assertEquals(self.calc.obtener_resultado(),1)

	def test_restar_6_menos_2_igual_1(self):
		self.calc.resta(6, 2)
		self.assertEquals(self.calc.obtener_resultado(),4)

	def test_restar_2_mas_3_igual_menos_1(self):
		self.calc.resta(2, 3)
		self.assertEquals(self.calc.obtener_resultado(),-1)

	def test_restar_l_menos_2_igual_dato_invalido(self):
		self.calc.resta('L', 2)
		self.assertEquals(self.calc.obtener_resultado(),'datos incorrectos')

	#multiplicacion
	def test_multiplicar_3_por_2_igual_6(self):
		self.calc.multiplicacion(3, 2)
		self.assertEquals(self.calc.obtener_resultado(),6)

	def test_multiplicar_3_por_menos_2_igual_menos_6(self):
		self.calc.multiplicacion(3, -2)
		self.assertEquals(self.calc.obtener_resultado(),-6)

	def test_multiplicar_menos_2_por_menos_4_igual_menos_8(self):
		self.calc.multiplicacion(-2, -4)
		self.assertEquals(self.calc.obtener_resultado(),8)

	def test_multiplicar_l_por_2_igual_dato_invalido(self):
		self.calc.multiplicacion('L', 2)
		self.assertEquals(self.calc.obtener_resultado(),'datos incorrectos')

	#division
	def test_dividir_6_entre_2_igual_6(self):
		self.calc.dividir(6, 2)
		self.assertEquals(self.calc.obtener_resultado(),3)

	def test_dividir_menos_4_entre_2_igual_menos_2(self):
		self.calc.dividir(-4, 2)
		self.assertEquals(self.calc.obtener_resultado(),-2)

	def test_dividir_menos_4_entre_menos_2_igual_menos_2(self):
		self.calc.dividir(-4, -2)
		self.assertEquals(self.calc.obtener_resultado(),2)

	def test_dividir_l_entre_2_igual_dato_invalido(self):
		self.calc.dividir('L', 2)
		self.assertEquals(self.calc.obtener_resultado(),'datos incorrectos')

	def test_dividir_3_entre_0_igual_dato_invalido_en_divisor(self):
		self.calc.dividir(3, 0)
		self.assertEquals(self.calc.obtener_resultado(),'datos invalido en divisor')	

	#Potencia
	def test_potencia_4_a_2_igual_16(self):
		self.calc.potencia(4, 2)
		self.assertEquals(self.calc.obtener_resultado(),16)

	def test_potencia_menos_4_a_2_igual_16(self):
		self.calc.potencia(-4, 2)
		self.assertEquals(self.calc.obtener_resultado(),16)

	def test_potencia_l_a_2_igual_dato_invalido(self):
		self.calc.potencia('L', 2)
		self.assertEquals(self.calc.obtener_resultado(),'datos incorrectos')

	#raiz
	def test_raiz_4_sobre_2_igual_2(self):
		self.calc.raiz(4, 2)
		self.assertEquals(self.calc.obtener_resultado(),2)

	def test_raiz_menos_4_sobre_2_igual_menos_2(self):
		self.calc.raiz(-4, 2)
		self.assertEquals(self.calc.obtener_resultado(),'No se puede sacar raiz a un num negativo')

	def test_raiz_l_a_2_igual_dato_invalido(self):
		self.calc.raiz('L', 2)
		self.assertEquals(self.calc.obtener_resultado(),'datos incorrectos')

if __name__ == '__main__':
	unittest.main()

