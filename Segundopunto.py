Numero1 = int(input("Ingresa el primer numero = "))
Numero2 = int(input("Ingresa el segundo numero = "))

condicion = lambda Numero1, Numero2: 1 if Numero1 > Numero2  else -1

calcular= condicion(Numero1, Numero2)

print("El primer numero es mayor que el segundo") if calcular == 1 else print("El pirmer numero es menor que el segundo")
