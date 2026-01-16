#Crear un programa que permita realizar las operaciones basicas +,-,*,/ utilizando un funciones para cada operacion y un menu principal para desplegar y elegir que operacion realizemos

print("Calculadora basica")
print("")

opcion = 0

while opcion != 5:
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir")
    print("")
    
    opcion = int(input("Elige una opcion: "))

    if opcion == 1:
        num1 = int(input("Ingresa el primer numero: "))
        num2 = int(input("Ingresa el segundo numero: "))
        resultado = num1 + num2
        print("La suma es:", resultado)

    else:
        if opcion == 2:
            num1 = int(input("Ingresa el primer numero: "))
            num2 = int(input("Ingresa el segundo numero: "))
            resultado = num1 - num2
            print("La resta es:", resultado)

        else:
            if opcion == 3:
                num1 = int(input("Ingresa el primer numero: "))
                num2 = int(input("Ingresa el segundo numero: "))
                resultado = num1 * num2
                print("La multiplicacion es:", resultado)

            else:
                if opcion == 4:
                    num1 = int(input("Ingresa el primer numero: "))
                    num2 = int(input("Ingresa el segundo numero: "))
                    
                    if num2 == 0:
                        print("No se puede dividir entre cero")
                    else:
                        resultado = num1 / num2
                        print("La division es:", resultado)

                else:
                    if opcion == 5:
                        print("Saliendo del programa...")
                    else:
                        print("Opcion no valida")

    print("")
