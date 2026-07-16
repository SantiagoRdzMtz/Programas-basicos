# Adivinar numero
import random

secreto = random.randint(1, 100)  # numero que el usuario debe adivinar

while True:  # se repite hasta que el usuario acierte (funciona como un do-while)
    intento = int(input("Adivina (1-100): "))

    if intento < secreto:
        print("Demasiado bajo")
    elif intento > secreto:
        print("Demasiado alto")
    else:
        print("¡Correcto! Era", secreto)
        break  # termina el bucle porque ya acerto

print("Juego terminado. El número era", secreto)