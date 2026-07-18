#Contar pares e impares
def contar_pares_impares(numeros):
    pares = 0
    impares = 0
    for num in numeros:
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares

numeros = []
for i in range(10):  # pide 10 numeros y los va guardando
    num = int(input("Número {}: ".format(i+1)))
    numeros.append(num)

p, i = contar_pares_impares(numeros)
print("Pares:", p)
print("Impares:", i)