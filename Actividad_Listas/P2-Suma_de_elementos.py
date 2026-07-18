#Suma de elementos 
def sumar_lista(lista):
    suma = 0
    for num in lista:
        suma += num  # va acumulando cada numero
    return suma

numeros = []
for i in range(5):
    valor = int(input(f"Ingrese número {i+1}: "))
    numeros.append(valor)

total = sumar_lista(numeros)
total_sum = sum(numeros)  

print("Suma con bucle:", total)
print("Suma con sum():", total_sum)