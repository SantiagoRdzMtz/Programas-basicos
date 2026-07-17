# Raiz cuadrada Newton-Raphson
import math

def raiz_newton(n, tolerancia=1e-10):
    if n < 0:
        raise ValueError("No se puede calcular raíz de negativo")  # no existe raiz real de un negativo
    estimacion = n / 2.0  # primera aproximacion
    while True:
        nueva = 0.5 * (estimacion + n / estimacion)  # formula de Newton-Raphson, mejora la estimacion
        if abs(nueva - estimacion) < tolerancia:
            return nueva  # se detiene cuando la mejora ya es minima
        estimacion = nueva

try:
    num = float(input("Número: "))
    r1 = math.sqrt(num)
    r2 = raiz_newton(num)
    print(f"math.sqrt: {r1}, Newton: {r2:.10f}")
    if abs(r1 - r2) < 1e-9:
        print("Resultados coinciden")
    else:
        print("Diferencia significativa")
except ValueError as e:
    print("Error:", e)