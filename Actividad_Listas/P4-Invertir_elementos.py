#Invertir elementos
def invertir_manual(lista):
    invertida = []
    for i in range(len(lista) - 1, -1, -1):  # recorre la lista de atras hacia adelante
        invertida.append(lista[i])
    return invertida

numeros = []
for i in range(6):
    valor = int(input(f"Número {i+1}: "))
    numeros.append(valor)

print("Original:", numeros)

invertida = invertir_manual(numeros)
print("Invertida:", invertida)