# 17Es primo
def es_primo(n):
    if n < 2:
        return False  # los numeros menores a 2 no son primos
    if n == 2:
        return True  # el 2 es el unico primo par, caso especial
    if n % 2 == 0:
        return False  # descarta los pares (menos el 2)
    for i in range(3, int(n ** 0.5) + 1, 2):  # prueba solo divisores impares hasta la raiz cuadrada
        if n % i == 0:
            return False
    return True

num = int(input("Ingrese un número: "))
if es_primo(num):
    print("Es primo")
else:
    print("No es primo")