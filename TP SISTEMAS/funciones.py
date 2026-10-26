def crear_pelicula(id, titulo, genero):
    dic = {
        "id": id,
        "titulo": titulo,
        "genero": genero,
        "notas": [],
        "actores": []
    }

    print("--- Datos ingresados ---")
    mostrar_diccionario(dic)
    return dic

def listar_peliculas(lista: list):
    if len(lista) == 0:
        print("No hay peliculas")
    else:
        cont = 0

        for elem in lista:
            print("id: ", cont)
            cont += 1
            mostrar_diccionario(elem)

def listar_titulos(lista: list):
    if len(lista) == 0:
        print("No hay peliculas")
    else:
        cont = 0

        for elem in lista:
            print("id: ", cont, " Titulo: ", elem["titulo"])
            cont += 1


def mostrar_diccionario(dic: dict):
    print("ID: ", dic["id"])
    print("Titulo: ", dic["titulo"])
    print("Genero: ", dic["genero"])

    if len(dic["notas"]) == 0:
        print("No hay puntuaciones")
    else:
        print("Puntuaciones: ")

        for elem in dic["notas"]:
            print("- ", elem)

    if len(dic["actores"]) == 0:
        print("No hay actores cargados")
    else:
        print("Actores: ")

        for elem in dic["actores"]:
            print("- ", elem)


def calcularPromedioLista(lista: list):
    suma = 0
    contador = 0

    if len(lista) > 0:
        for elem in lista:
            suma += elem
            contador += 1

        promedio = suma / contador
        return promedio

    else:
        print("No hay elementos")
        return 0


