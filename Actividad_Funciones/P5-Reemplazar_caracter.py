# Reemplazar caracter
def reemplazar_manual(texto, viejo, nuevo):
    if len(viejo) != 1 or len(nuevo) != 1:
        return texto, 0  # solo acepta un caracter, si no, no hace cambios
    resultado = ""
    contador = 0
    for letra in texto:
        if letra == viejo:
            resultado += nuevo
            contador += 1  # cuenta cada vez que se hace un cambio
        else:
            resultado += letra
    return resultado, contador

texto = input("Cadena: ")
car_viejo = input("Carácter a reemplazar: ")
car_nuevo = input("Carácter nuevo: ")

if len(car_viejo) != 1 or len(car_nuevo) != 1:
    print("Debe ingresar un solo carácter")
else:
    texto_mod, num = reemplazar_manual(texto, car_viejo, car_nuevo)
    texto_mod2 = texto.replace(car_viejo, car_nuevo)  # forma rapida usando la funcion de python
    print("Manual:", texto_mod, "| Reemplazos:", num)
    print("Con replace:", texto_mod2)
    if texto_mod == texto_mod2:
        print("Correcto")  # confirma que ambos metodos dan el mismo resultado