Feature: Division de dos numeros
	Como usuario de la calculadora
	deseo realizar la Multiplicacion de dos numeros
	para obtener el resultado preciso


	Scenario: Division de 2 entre dos
		Dado que ingreso los numeros "2" entre "2"
		cuando realizo la operación
		entonces obtengo el resultado "1"

	Scenario: Division de 15 entre tres
		Dado que ingreso los numeros "15" entre "3"
		cuando realizo la operación
		entonces obtengo el resultado "5"

	Scenario: Division de 0 entre 7
		Dado que ingreso los numeros "0" entre "7"
		cuando realizo la operación
		entonces obtengo el resultado "0"