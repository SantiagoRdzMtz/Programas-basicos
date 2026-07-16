#Calculadora Básica
while True:  # simula un do-while, siempre entra al menos una vez
    print("1.Suma 2.Resta 3.Multiplicación 4.División 5.Salir")  # menu de opciones
    op = int(input("Opción: "))

    if op == 5:  # si elige 5 se sale del programa
        break

    num1 = float(input("Primer número: "))  # pido el primer numero
    num2 = float(input("Segundo número: "))  # pido el segundo numero

    match op:  # match-case segun la opcion elegida
        case 1: print(num1 + num2)
        case 2: print(num1 - num2)
        case 3: print(num1 * num2)
        case 4:
            if num2 != 0:  # revisa que no sea division entre 0
                print(num1 / num2)
            else:
                print("Error: división por cero")

    resp = input("¿Desea continuar? (s/n): ").lower()  # pregunta si sigue o no
    if resp == 'n':
        break  # se detiene si respondio n