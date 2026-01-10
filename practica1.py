#Operacion de multiplicacion con sumas

print("Multiplicacion")
print("")

num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))

resultado = 0
contador = 0
operacion = ""

while contador < num1:
    resultado = resultado + num2
    operacion = operacion + str(num2)
    
    if contador < num1 - 1:
        operacion = operacion + " + "
        
    contador = contador + 1

print("")
print("La multiplicacion de {0} por {1} es: {2}".format(num1, num2, resultado))
print("Operacion realizada:")
print(operacion)
