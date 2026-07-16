#Media de numeros positivos
suma = 0  # aqui se va acumulando la suma de los positivos
contador = 0  # cuenta cuantos positivos se ingresaron

while True:  # se repite hasta que metan un negativo
    num = float(input("Número positivo (negativo sale): "))
    if num < 0:
        break  # termina el programa si es negativo

    if num > 0:
        suma += num  # se suma el numero
        contador += 1  # se cuenta uno mas

if contador > 0:
    media = suma / contador  # promedio de los positivos
    print("Media:", media)
else:
    print("No se ingresaron positivos")  # evita dividir entre 0