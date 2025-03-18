def mostrarMenu():
    print("\nOpciones:")
    print("1. addmultiplenumbers")
    print("2. multiplymultiplenumbers")
    print("3. isiteven")
    print("4. isitaninteger")
    print("5. Exit")


def addmultiplenumbers(lista):
    return sum(lista)


def multiplymultiplenumbers(lista):
    resultado = 1
    for num in lista:
        resultado *= num
    return resultado


# def isiteven(num):
#   input("Ingrese un numero para saber si: True` si el número es par o entero, `False` en caso contrario:  "))
#   if num % 2 == 0:
#     return(True)
#   else:
#       return(False)


#! Autoria de ana
def isiteven(num):
    if num % 2 == 0:
        return True
    else:
        return False


# def isitaninteger():
#     num = input("Ingresa un número: ")
#     if num.lstrip("-").isdigit():
#         num = int(num)
#         return(True)
#     else:
#         return(False)


#! Ana
def isitaninteger(num):
    if num.is_integer():
        return True
    else:
        return False


def main():
    while True:
        mostrarMenu()
        try:
            opcion = input("Ingrese su opción: ")

            if opcion == "1":
                numeros = [4, -5, 6.7]
                addmultiplenumbers(numeros)

            elif opcion == "2":
                numeros = [4, -5, 6.7]
                multiplymultiplenumbers(numeros)

            elif opcion == "3":
                num = float(input("Ingrese un número: "))
                resultado = isiteven(num)
                print(f"El número es par: {resultado}")

            elif opcion == "4":
                num = float(input("Ingrese un número: "))
                resultado = isitaninteger(num)
                print(f"El número es entero: {resultado}")

            else:
                print("Opción inválida. Por favor, elija una opción válida.")
        except ValueError:
            print("Error")


if __name__ == "__main__":
    main()
