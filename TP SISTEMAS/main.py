from funciones import *

lista_bd = []


def menu():
    print("1. Crear pelicula")
    print("2. Listar peliculas")
    print("3. Ingresar puntuacion")
    print("4. Calcular promedio individual")
    print("5. Agregar actor a pelicula")
    print("6. Mostrar actores de pelicula")

    op = int(input("Ingrese una opcion: "))

    return op

while True:
    op = menu()

    if op == 1:
        id = len(lista_bd) + 10000
        titulo = input("Ingrese el titulo: ")
        genero = input("Ingrese el genero: ")

        pelicula = crear_pelicula(id, titulo, genero)

        lista_bd.append(pelicula.copy())

    elif op == 2:
        listar_peliculas(lista_bd)

    elif op == 3:
        listar_titulos(lista_bd)

        id = int(input("Ingrese el id correspondiente: "))
        nota = int(input("Ingrese la puntuacion: "))

        lista_bd[id]["notas"].append(nota)

    elif op == 4:
        listar_titulos(lista_bd)

        id = int(input("Ingrese el id correspondiente: "))
        promedio = calcularPromedioLista(lista_bd[id]["notas"])
        print("El promedio es: ", promedio)

    elif op == 5:
        listar_titulos(lista_bd)

        id = int(input("Ingrese el id correspondiente: "))
        actor = input("Ingrese el nombre del actor: ")

        lista_bd[id]["actores"].append(actor)

    elif op == 6:
        listar_titulos(lista_bd)

        id = int(input("Ingrese el id correspondiente: "))

        print("Actores de la pelicula:")

        for actor in lista_bd[id]["actores"]:
            print("- ", actor)

    else:
        print("Opcion incorrecta")