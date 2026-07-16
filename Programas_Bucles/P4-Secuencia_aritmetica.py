# Secuencia aritmetica
inicio = int(input("Primer número: "))
diferencia = int(input("Diferencia: "))
limite = int(input("Límite máximo: "))

num = inicio
while True:  # simula un do-while, siempre entra al menos una vez
    print(num, end=" ")
    num += diferencia  # avanza al siguiente numero de la secuencia
    if num > limite:
        break  # se detiene cuando el numero ya paso el limite

print("\nSecuencia aritmética desde", inicio, "hasta", limite)