# Conteo de números
n = int(input("Cantidad de números a ingresar: "))  # cuantos numeros va a ingresar el usuario

mayores = 0  # contador de numeros mayores a 0
menores = 0  # contador de numeros menores a 0
iguales = 0  # contador de numeros iguales a 0

for i in range(n):  # se repite n veces, una por cada numero
    num = int(input("Número: "))

    if num > 0:
        mayores += 1
    elif num < 0:
        menores += 1
    else:
        iguales += 1

# al final se muestran los resultados
print("Mayores a 0:", mayores)
print("Menores a 0:", menores)
print("Iguales a 0:", iguales)