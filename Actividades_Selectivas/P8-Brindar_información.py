#Brindar información
consulta = input("Ingrese nombre de artista, película o serie: ").lower()
match consulta:
    case "inception":
        info = "Película de ciencia ficción dirigida por Christopher Nolan."
    case "beatles":
        info = "Banda británica de rock formada en 1960."
    case "rick and morty":
        info = "Serie animada de comedia y ciencia ficción."
    case "stranger things":
        info = "Serie de terror y ciencia ficción de Netflix."
    case "avengers":
        info = "Película de superhéroes del MCU."
    case _:
        info = "No se encontró información."
print("Información:", info)