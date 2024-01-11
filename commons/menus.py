### Importaciones ###

from utils import validar_opcion

### Menus del programa MAIN ###

def menu_principal():
    print("----------- Menú Principal-----------")
    print("1. Peliculas")
    print("2. Gestion de peliculas")
    print("3. Salir")   
    op=validar_opcion("Opcion: ",1,3)
    return op

def menu_peliculas():
    print("----------- Menú Peliculas-----------")
    print("1. Listar peliculas")
    print("2. Buscar pelicula por nombre")
    print("3. Buscar pelicula por nombre de los actores")
    print("4. Buscar peliculas por personaje de la pelicula")
    print("5. Buscar peliculas por genero")
    print("6. Buscar peliculas por código")
    op=validar_opcion("Opcion: ",1,6)
    return op

def gestion_peliculas():
    print("----------- Menú Gestion Peliculas-----------")
    print("1. Agregar pelicula")
    print("2. Modificar pelicula")
    print("3. Eliminar pelicula")
    print("4. Salir")
    op=validar_opcion("Opcion: ",1,4)
    return op