#Convertir a mayusculas
def main():
    contador = 0
    while True:
        entrada = input("Palabra o número (espacio termina): ")
        if entrada == " ":
            break # termina el programa cuando se ingresa un espacio
        try:
            if entrada.isdigit():
                entrada = str(entrada)  # convierte a string si es un numero
            print(entrada.upper())  # imprime en mayusculas
            contador += 1
        except Exception as e:
            print("Error:", e)
    print("Programa terminado")
    print("Cantidad de palabras procesadas:", contador)

main()