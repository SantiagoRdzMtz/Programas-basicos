# Palindromo
def es_palindromo(texto):
    texto = texto.lower()  # convierte todo a minusculas
    limpio = ""
    for caracter in texto:
        if caracter != " ":
            limpio += caracter  # va armando la cadena sin espacios
    return limpio == limpio[::-1], limpio  # regresa si es palindromo y la cadena limpia (agregue lo ultimo para que funcione correctamente)

entrada = input("Ingrese una frase: ")
resultado, cadena_limpia = es_palindromo(entrada)
if resultado:
    print("Es un palíndromo")
else:
    print("No es palíndromo")
print("Longitud de la cadena limpia:", len(cadena_limpia))