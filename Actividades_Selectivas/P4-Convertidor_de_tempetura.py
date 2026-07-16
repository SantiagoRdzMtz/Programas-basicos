#Convertidor de tempetura
celsius = float(input("Temperatura en °C: "))
print("1. Fahrenheit\n2. Kelvin")
opcion = int(input("Elige opción: "))
match opcion:
    case 1:
        resultado = celsius * 9/5 + 32
        unidad = "°F"
    case 2:
        resultado = celsius + 273.15
        unidad = "K"
    case _:
        resultado = None
        print("Opción inválida")
if resultado is not None:
    print("Convertido:", resultado, unidad)