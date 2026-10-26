def mostrar_menu():
    print("1 agregar nota")
    print("2 ver notas")
    print("3 calcular promedio")
    print("4 buscar nota mayor")
    print("5 calcular media")
    print("6 ver solamente notas impares")
    print("7 salir")
    opcion=int(input("ingrese la opcion"))
    if opcion <=7:
        if opcion >=1:
            return opcion 
def verificar_nota (nota):
        if nota >=1 and nota <=10:
            return True
        else:
            return False
def mostar_lista(lista):
        for nota in lista:
            print(nota)
def calcular_promedio(lista):
     suma=0
     for nota in lista:
        suma = suma + nota
        promedio = suma / len(lista)        
        return promedio
def buscar_nota_mayor(lista):
     mayor=lista[0]
     for nota in lista:
          if nota > mayor:
               mayor = nota
     return mayor
def calcular_media(lista):
    suma = 0
    for nota in lista:
        suma = suma + nota
    media = suma / len(lista)
    return media
def notas_impares(lista):
     impares = []
     for nota in lista:
          if nota % 2!=0:
               impares.append(nota)
     return impares
               
     
