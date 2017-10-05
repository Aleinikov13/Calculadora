Feature: Potencia de dos numeros
	Como usuario de la calculadora
	deseo realizar la Potencia de dos numeros
	para obtener el resultado preciso


	Scenario: Potencia de 2 a la dos
		Dado que ingreso los numeros "2" a la "2"
		cuando realizo la operación
		entonces obtengo el resultado "4"

	Scenario: Potencia de 3 a la tres
		Dado que ingreso los numeros "3" a la "3"
		cuando realizo la operación
		entonces obtengo el resultado "27"

	Scenario: Potencia de 0 a la 7
		Dado que ingreso los numeros "0" a la "7"
		cuando realizo la operación
		entonces obtengo el resultado "0"