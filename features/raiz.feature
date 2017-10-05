Feature: Raiz de dos numeros
	Como usuario de la calculadora
	deseo realizar la Raiz de dos numeros
	para obtener el resultado preciso


	Scenario: Raiz de 4 de dos
		Dado que ingreso los numeros "4" de "2"
		cuando realizo la operación
		entonces obtengo el resultado "2"

	Scenario: Raiz de 16 de 4
		Dado que ingreso los numeros "16" entre "4"
		cuando realizo la operación
		entonces obtengo el resultado "4"

	Scenario: Raiz de 0 de 7
		Dado que ingreso los numeros "0" de "7"
		cuando realizo la operación
		entonces obtengo el resultado "0"