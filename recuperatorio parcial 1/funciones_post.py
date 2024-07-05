""""RECUPERATORIO PRIMER PACRIAL PROGRAMACION 2024
Alumno: Osorio Brenda
Division: 113"""

import os
from random import randint
import json

def get_path_actual(nombre_archivo: str)-> str:
    """Funcion que nos devuelva la ruta completa del archivo

    Args:
        nombre_archivo (str): recibe el nombre de un archivo

    Returns:
        str: ruta actual del archivo
    """
    import os
    directorio_actual = os.path.dirname(__file__)
    return os.path.join(directorio_actual, nombre_archivo)


#punto 1

def abrir_archivo(archivo:str)-> list: 
    """Funcion para abrir el archivo .csv que nos ingrese el usuario por conosla.

    Args:
        Recibe de parametro, el nombre del archivo que queremos abrir.
    
    Returns:
        Nos devuelve una lista de diccionarios, sobre la que podemos trabajar.

    """
    ruta_archivo = get_path_actual(f"{archivo}.csv")
    if not os.path.exists(ruta_archivo):
        print("ruta de archivo no encontrada")
    else:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo: #siempre agregar "r"/"w" y el encoding utf-8
            lista_usuario = []
            encabezado = archivo.readline().strip("\n")
            
            encabezado = encabezado.split(",") #uso el caracter que yo quiera (en este caso ,) como separador
            #encabezado = archivo.readline().strip("\n").split(",") otra opcion 

            for linea in archivo.readlines():
                usuario = {}
                linea = linea.strip("\n").split(",")
                
                id, user, likes, dislikes, followers = linea
                usuario["id"] = int(id)
                usuario["user"] = user
                usuario["likes"] = float(likes)
                usuario["dislikes"] = float(dislikes)
                usuario["followers"] = int(followers)
                lista_usuario.append(usuario)
        return lista_usuario

#punto 2

def mostrar_usuario(lista_usuario: list):
    """Funcion que nos muestra un encabezado con el ID; USER, LIKES, DISLIKES, FOLLOWERS

    Args:
        lista que nos devolvio al cargar el archivo.
    """
    print(f"{lista_usuario["id"]}, {lista_usuario["user"]:12}, {lista_usuario["likes"]:>10}, {lista_usuario["dislikes"]:>12}, {lista_usuario["followers"]:>15}")


def mostrar_posteos(lista_usuario: list):
    """Funcion que nos muestra los usuario debajo del encabezado.

    Args:
        Lista que nos devuelve en el punto 1
    """
    tam = len(lista_usuario)
    print("                   LISTA USUARIO                      ")
    print("ID      USER         LIKES          DISLIKES          FOLLOWERS   ")

    for i in range(tam):
        mostrar_usuario(lista_usuario[i])
    print()


#punto 3

def asignar_estadisticas(lista: list)-> list:
    """Funcion para asignar likes, dislikes yfollowers a cada usuario.

    Args:
        Recibe una lista con los datos de los usuarios.

    Returns:
        Devuelve la misma lista pero modificada.
    """
    
    for el in lista:
        el["likes"] = randint(500, 3000) #cuando me paro en el elemento correspondiente a la llave, me modifica el valor a los paramteros que yo di
        el["dislikes"] = randint(300, 3500)
        el["followers"] = randint(10000, 20000)
    return lista

#punt0 4

def crear_archivo(archivo:str, lista:list):
    """Funcion para separar a los usuarios en diferentes archivos, segun su cantidad de likes o dislikes.

    Args:
        Recibe un string con el nombre que tendra el archivo.
        Recibe una lista con los datos de los usuarios.
    """

    with open(get_path_actual(f"{archivo}.csv"), "w", encoding="utf-8") as archivo:
        encabezado = ["id", "user", "likes", "dislikes", "followers"]

        archivo.write(",".join(encabezado) + "\n")

        for i in lista:
            linea_elemento = f"{i["id"]},{i["user"]},{i["likes"]},{i["dislikes"]},{i["followers"]}" + "\n"
            archivo.write(linea_elemento)


def filtrar_por_likes(lista:list):
    """Funcion que nos filtra la lista segun el parametro.

    Args:
        Recibe una lista con los usuarios y sus datos.
        Recibe un string con la llave sobre la que se va a filtrar.
    """
    lista_filtrada = []
    #minimo_de_likes = 2000

    for i in lista:
        if i["likes"] > 2000:
            lista_filtrada.append(i)
             
    crear_archivo("likes", lista_filtrada)


#punto 5

def filtrar_por_dislike(lista: list):
    lista_dislike = []

    for i in lista:
        if i["dislikes"] > i["likes"]:
            lista_dislike.append(i)
            print(lista_dislike)
    crear_archivo("dislikes", lista_dislike)


#punto 6

def promedio_followers(lista: list)-> int:
    acumulador_seguidores = 0
    acumulador_posts = 0

    for el in lista:
        if el["followers"] > 0:
            acumulador_seguidores += el["followers"]
            acumulador_posts += 1

    promedio = int(acumulador_seguidores/acumulador_posts)
    print(f"el promedio de seguidores es {promedio}")

    return acumulador_seguidores


#punto 7

def swap_lista(lista:list, i: int, j:int):
    """Funcion que nos compara dos elementos de una lista y los cambia de lugar uno con el otro.

    Args:
        Recibe una lista con los datos de los competidores.
        Recibe un parametro i (un entero) que es la posicion del elemento en la lista. 
        Recibe un parametro J (un entero) que es la posicion del elemento en la lista. 
    """
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux


def ordenar_por_criterio(lista:list, criterio:str):
    """Funcion para ordenar una lista mediante un criterio.

    Args:
        Recibe una lista con los datos de los posts.
        Recibe un criterio en formato string.
    """
    tam = len(lista)

    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if lista[i][criterio] > lista[j][criterio]:
                    swap_lista(lista, i, j)
                    

def cargar_archivo_json(lista:list, nombre_archivo: str):
    """Funcion para cargar un archivo .json con los datos ordenados.

    Args:
        Recibe una lista con los posteos y sus datos (sin ordenar)
        Recibe un string con el nombre del archivo que queremos que tenga.
    """
    lista_ordenada = []
    lista_ordenada.append(ordenar_por_criterio(lista, "user"))
    with open(get_path_actual(f"{nombre_archivo}.json"), "w", encoding="utf-8") as archivo:
        json.dump(lista, archivo, ensure_ascii = False, indent = 4)
    

#punto 8

def calcular_mayor(lista:list)-> int:
    """Funcion para calcular el numero mayor de una lista.

    Args:
        Recibe una lista con los datos de los posteos.

    Returns:
        Nos devuelve un entero, que es el mayor de la lista.
    """
    
    numero_mayor = lista[0]["likes"]

    for i in lista:
        if i["likes"] > numero_mayor:
           numero_mayor = i["likes"]
    return numero_mayor


def informar_posteo_mas_likeado(lista:list):
    """Funcion que nos infroma el nombre y la cantidad de likes del mejor posteo.

    Args:
        Recibe una lista con todos los datos de los posteos.
      
    """
    posteo_maximo = calcular_mayor(lista)
    lista_mas_likeados = []

    for i in lista:
        if i["likes"] == posteo_maximo:
            lista_mas_likeados.append(i)
            print(f"Nombre usuario: {i["user"]}, cantidad de likes {i["likes"]}")

    if len(lista_mas_likeados) > 1:
        print("  EMPATE  ")


def pausar():
    """Funcion que pause el programa 
    hasta que el usuario presione alguna tecla.
    """
    os.system("pause")


def menu():
    """Funcion que del menu con sus opciones.

    Returns:
        Devuelve una variable de tipo string.
    """
    print("RED SOCIAL 2024")
    print("-----------------------------")
    print("Elija una opción")
    print("1) Cargar archivo .csv")
    print("2) Imprimir tabla de datos")
    print("3) Ver estadisticas de usuarios")
    print("4) Filtrar mejores posts")
    print("5) filtrar peores post")
    print("6) Listado de promedio de seguidores")
    print("7) Listado de usuarios en forma ascendente (se crea archivo .json)")
    print("8) Informar posteo/s mas gustado/s")
    print("9) Salir")

    opcion = input("Ingrese una opción (solo un numero por vez): ")

    return opcion


def limpiar_terminal():
    """Funcion que nos limpia la terminal.
    """
    os.system("cls")