Feature: Resta de dos numeros
	Como usuario de la calculadora
	deseo realizar la resta de dos numeros
	para obtener el resultado preciso


	Scenario: Resta de 2 menos dos
		Dado que ingreso los numeros "2" - "2"
		cuando realizo la operación
		entonces obtengo el resultado "0"

	Scenario: Resta de 7 menos cinco
		Dado que ingreso los numeros "7" - "5"
		cuando realizo la operación
		entonces obtengo el resultado "2"

	Scenario: Resta de 0 mas 7
		Dado que ingreso los numeros "0" - "7"
		cuando realizo la operación
		entonces obtengo el resultado "-7"