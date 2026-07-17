#Máximo Común Divisor
import math

def mcd(a, b):
    a = abs(a)  # convierte a positivo por si el numero es negativo
    b = abs(b)
    if a == 0 and b == 0:
        return 0  # caso especial: si ambos son cero, no hay MCD real
    while b != 0:
        a, b = b, a % b  # va reduciendo los numeros usando el residuo
    return a

num1 = int(input("Primer número: "))
num2 = int(input("Segundo número: "))

resultado = mcd(num1, num2)
resultado_math = math.gcd(num1, num2)  # se usa para verificar que el resultado sea correcto

print(f"MCD calculado: {resultado}")
print(f"MCD con math.gcd: {resultado_math}")
print("Los resultados sí coinciden" if resultado == resultado_math else "No coinciden")

if num1 == 0 and num2 == 0:
    print("Caso especial: ambos números son cero")
else:
    print("Programa terminado")