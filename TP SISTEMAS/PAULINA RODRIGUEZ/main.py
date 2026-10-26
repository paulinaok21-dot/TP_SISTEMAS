from funciones import*
from funcionesn import*
lista = []
while True:
    opcion = mostrar_menu()
    if opcion == 1:
        usu=int(input("ingrese un numero"))

        if verificar_nota(usu):
            lista.append(usu)
            print("nota agregada")
        else:
            print("nota incorrecta")
    elif opcion == 2:
        mostrar_lista(lista)

    elif opcion == 3:
        promedio=calcular_promedio(lista)
        print("el promedio es",promedio)

    elif opcion == 4:
        mayor = buscar_nota_mayor(lista)
        print("la nota mayor es",mayor)

    elif opcion == 5:
        media = calcular_media(lista)
        print("la media es", media)

    elif opcion == 6:
        impares=notas_impares(lista)
        mostrar_lista(impares)

    elif opcion == 7:
        print("salir")
        break
    else:
        print("opcion incorrecta")
