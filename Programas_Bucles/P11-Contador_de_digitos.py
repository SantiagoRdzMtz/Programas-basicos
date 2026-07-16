#Contador de digitos
num = int(input("Número entero: "))
if num == 0:
    digitos = 1
else:
    digitos = 0
    if num < 0:
        num = abs(num)  # convierte el negativo a positivo
    while num != 0:
        num //= 10  # le quita un digito en cada vuelta
        digitos += 1
print("El número tiene", digitos, "dígitos")