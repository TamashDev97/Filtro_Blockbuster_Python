### Importaciones ###
import json
import os

################# Funciones JSON para cargar el archivo peliculas.json ########################################

def cargarPeliculas_json():
    try:
        file_path = os.path.join("data", "peliculas.json")
        with open(file_path, 'r') as archivo_json:
            lista_peliculas = json.load(archivo_json)
            print("La lista de peliculas ha sido cargada correctamente.")
            return lista_peliculas
    except FileNotFoundError:
        print("El archivo 'peliculas.json' no existe. Devolviendo una lista vacía.")
        return []
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return []

lista_peliculas = cargarPeliculas_json()


########################### Funciones de peliculas ###########################

### Función para imprimir las peliculas ###

def imprimir_pelicula(pelicula):
    print(f"Nombre: {pelicula['titulo']}")
    print(f"Duración: {pelicula['duracion']}")
    print(f"Género: {pelicula['genero']['nombre']}")
    print("Actores principales:")
    for id_actor, actor in pelicula['actores'].items():
        print(f"  - {actor['nombre']} {actor['apellido']}, Rol: {actor['rol']}")
    print("Formatos disponibles:")
    for id_formato, formato in pelicula['formato'].items():
        print(f"  - {formato['nombre']}, Precio del alquiler: {formato['precio_del_alquiler']}, Cantidad: {formato['cantidad']}")
    print(f"Sinopsis: {pelicula['sinopsis']}")
    print("\n")


### Funciones para listar las peliculas ###

def listar_peliculas(lista_peliculas):
    for pelicula in lista_peliculas:
        print(f"Nombre: {pelicula['nombre']}")
        print(f"Duración: {pelicula['duracion']}")
        print(f"Género: {pelicula['genero']}")
        print("Actores principales:")
        for actor in pelicula['actores_principales']:
            print(f"  - {actor}")
        print("Formatos disponibles:")
        for formato in pelicula['formatos_disponibles']:
            print(f"  - {formato}")
        print(f"Sinopsis: {pelicula['sinopsis']}")
        print("\n")

listar_peliculas(lista_peliculas)

### Funciones para buscar peliculas en el catalogo ###

def buscar_pelicula_nombre(lista_peliculas, nombre_pelicula):
    for id_pelicula, pelicula in lista_peliculas.items():
        if nombre_pelicula.lower() in pelicula['titulo'].lower():
            imprimir_pelicula(pelicula)

### Buscar pelicula por nombre de los actores ###

def buscar_pelicula_actor(lista_peliculas, nombre_actor):
    nombre_actor = nombre_actor.lower()
    for id_pelicula, pelicula in lista_peliculas.items():
        for id_actor, actor in pelicula['actores'].items():
            if nombre_actor in (actor['nombre'] + " " + actor['apellido']).lower():
                imprimir_pelicula(pelicula)
                break


### Buscar peliculas por personaje de la pelicula ###

def buscar_pelicula_personaje(lista_peliculas, nombre_personaje):
    nombre_personaje = nombre_personaje.lower()
    for id_pelicula, pelicula in lista_peliculas.items():
        for id_actor, actor in pelicula['actores'].items():
            if nombre_personaje in actor['rol'].lower():
                imprimir_pelicula(pelicula)
                break
            
### Buscar peliculas por genero de pelicula ###

def buscar_pelicula_genero(lista_peliculas, genero_pelicula):
    genero_pelicula = genero_pelicula.lower()
    for id_pelicula, pelicula in lista_peliculas.items():
        if genero_pelicula in pelicula['genero']['nombre'].lower():
            imprimir_pelicula(pelicula)

### Buscar peliculas por codigo ###

def buscar_pelicula_codigo(lista_peliculas, codigo_pelicula):
    codigo_pelicula = codigo_pelicula.lower()
    for id_pelicula, pelicula in lista_peliculas.items():
        if codigo_pelicula == id_pelicula.lower():
            imprimir_pelicula(pelicula)
            break