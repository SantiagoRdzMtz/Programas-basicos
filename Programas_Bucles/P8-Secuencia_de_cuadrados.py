#Secuencia de cuadrados
N = int(input("Número positivo: "))
i = 1

while True:  # emula un do-while, siempre entra al menos una vez
    print(i ** 2)  # imprime el cuadrado de i
    i += 1  # avanza al siguiente numero
    if i > N:
        break  # se detiene cuando ya se paso del limite

print("Secuencia de cuadrados hasta", N)