def menu ():
    opcion=int(input("ingrese una opcion"))
    if opcion <=7:
        if opcion >=1:
            return opcion
def verificar_nota(nota):
    if nota >7 and nota <10:
        return True
    else:
     return False
def mostrar_lista(lista):
    for nota in lista:
        print(nota)
    