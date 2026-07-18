#Encontrar mayor y menor
def maximo_manual(lista):
    if len(lista) == 0:
        return None
    maximo = lista[0]  # empieza suponiendo que el primero es el mayor
    for num in lista[1:]:
        if num > maximo:
            maximo = num
    return maximo

def minimo_manual(lista):
    if len(lista) == 0:
        return None
    minimo = lista[0]  # empieza suponiendo que el primero es el menor
    for num in lista:
        if num < minimo:
            minimo = num
    return minimo

numeros = []
for i in range(8):
    valor = int(input(f"Número {i+1}: "))
    numeros.append(valor)

mayor_manual = maximo_manual(numeros)
menor_manual = minimo_manual(numeros)

mayor_builtin = max(numeros)  # usando la funcion de python
menor_builtin = min(numeros)

print("Mayor (manual):", mayor_manual)
print("Menor (manual):", menor_manual)
print("Mayor (built-in):", mayor_builtin)
print("Menor (built-in):", menor_builtin)