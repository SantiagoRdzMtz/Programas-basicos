# Contador de numeros impares
N = int(input("Número positivo: "))
i = 1

while True:  # simula un do-while, siempre entra al menos una vez
    if i % 2 != 0:  # revisa si i es impar
        print(i, end=" ")
    i += 1
    if i > N:
        break  # se detiene cuando ya se paso del limite

print("\nFin. Se mostraron los impares hasta", N)