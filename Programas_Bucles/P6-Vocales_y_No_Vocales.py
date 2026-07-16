# Vocales / No Vocales
while True:
    letra = input("Ingrese letra (espacio termina): ")
    if letra == " ":
        break  # termina el programa cuando el usuario ingresa un espacio
    letra = letra.lower()  # convierte a minuscula para que funcione con mayus y minus
    if letra in "aeiou":
        print("Vocal")
    else:
        print("Consonante")

print("Programa finalizado")