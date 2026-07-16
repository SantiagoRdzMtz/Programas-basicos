#Factorial
num = int(input("Número para factorial: "))  # pido el numero al usuario
factorial = 1  # aqui se va guardando el resultado

if num < 0:  # valida que no sea negativo
    print("Factorial no definido para negativos")
else:
    for i in range(1, num + 1):  # recorre del 1 hasta el numero
        factorial *= i  # va multiplicando en cada vuelta
    print("El factorial de", num, "es:", factorial)