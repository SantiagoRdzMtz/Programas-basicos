# Contar letras a
palabra = input("Ingrese una palabra: ").lower()  # se pasa a minusculas para que 'A' cuente igual que 'a'
contador = 0

for letra in palabra:  # recorre la palabra letra por letra
    if letra == 'a':
        contador += 1  # suma 1 cada vez que encuentra una 'a'

print("La letra 'a' aparece", contador, "veces")