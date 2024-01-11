### Importaciones ###
import json
import os

################# Funciones JSON para cargar y guardar el archivo peliculas.json ########################################

### Función para cargar el archivo peliculas.json ###

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

### Función para guardar el archivo peliculas.json ###

def guardarPeliculas_json(lista_peliculas):
    try:
        file_path = os.path.join("data", "peliculas.json")
        with open(file_path, 'w') as archivo_json:
            json.dump(lista_peliculas, archivo_json)
            print("La lista de películas ha sido guardada correctamente.")
    except FileNotFoundError:
        print("El directorio 'data' no existe. Por favor, crea el directorio antes de guardar.")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")
        

################# Funciones de gestión de peliculas ########################################

### Función para agregar las peliculas al catalogo ###

def recoger_genero():
    id_genero = input("Introduce el ID del género: ")
    nombre = input("Introduce el nombre del género: ")
    return {"id_genero": id_genero, "nombre": nombre}

def recoger_actores():
    actores = {}
    while True:
        id_actor = input("Introduce el ID del actor (o 'q' para terminar): ")
        if id_actor.lower() == 'q':
            break
        nombre = input("Introduce el nombre del actor: ")
        apellido = input("Introduce el apellido del actor: ")
        rol = input("Introduce el rol del actor: ")
        actores[id_actor] = {"id_actor": id_actor, "nombre": nombre, "apellido": apellido, "rol": rol}
    return actores

def recoger_formatos():
    formatos = {}
    while True:
        id_formato = input("Introduce el ID del formato (o 'q' para terminar): ")
        if id_formato.lower() == 'q':
            break
        nombre = input("Introduce el nombre del formato: ")
        precio_del_alquiler = input("Introduce el precio del alquiler: ")
        cantidad = input("Introduce la cantidad: ")
        formatos[id_formato] = {"id_formato": id_formato, "nombre": nombre, "precio_del_alquiler": precio_del_alquiler, "cantidad": cantidad}
    return formatos

def agregar_pelicula(lista_peliculas):
    id_pelicula = input("Introduce el ID de la película: ")
    titulo = input("Introduce el nombre de la película: ")
    duracion = input("Introduce la duración de la película: ")
    sinopsis = input("Introduce la sinopsis de la película: ")
    genero = recoger_genero()
    actores = recoger_actores()
    formato = recoger_formatos()
    lista_peliculas[id_pelicula] = {
        "id_pelicula": id_pelicula,
        "titulo": titulo,
        "duracion": duracion,
        "sinopsis": sinopsis,
        "genero": genero,
        "actores": actores,
        "formato": formato
    }
    guardarPeliculas_json(lista_peliculas)

### Función para modificar las peliculas del catalogo ###

def recoger_datos_pelicula():
    titulo = input("Introduce el nombre de la película: ")
    duracion = input("Introduce la duración de la película: ")
    while not duracion.isdigit() or int(duracion) <= 0:
        print("La duración debe ser un número positivo.")
        duracion = input("Introduce la duración de la película: ")
    sinopsis = input("Introduce la sinopsis de la película: ")
    genero = recoger_genero()
    actores = recoger_actores()
    formato = recoger_formatos()
    return titulo, duracion, sinopsis, genero, actores, formato


def modificar_pelicula(lista_peliculas):
    id_pelicula = input("Introduce el ID de la película que quieres modificar: ")
    if id_pelicula not in lista_peliculas:
        print("No se encontró ninguna película con ese ID.")
        return
    print("Deja el campo en blanco si no quieres modificarlo.")
    titulo, duracion, sinopsis, genero, actores, formato = recoger_datos_pelicula()
    if titulo:
        lista_peliculas[id_pelicula]['titulo'] = titulo
    if duracion:
        lista_peliculas[id_pelicula]['duracion'] = duracion
    if sinopsis:
        lista_peliculas[id_pelicula]['sinopsis'] = sinopsis
    if genero:
        lista_peliculas[id_pelicula]['genero'] = genero
    if actores:
        lista_peliculas[id_pelicula]['actores'] = actores
    if formato:
        lista_peliculas[id_pelicula]['formato'] = formato
    guardarPeliculas_json(lista_peliculas)


### Función para eliminar las peliculas del catalogo ###

def eliminar_pelicula(lista_peliculas):
    id_pelicula = input("Introduce el ID de la película que quieres eliminar: ")
    if id_pelicula not in lista_peliculas:
        print("No se encontró ninguna película con ese ID.")
        return
    del lista_peliculas[id_pelicula]
    guardarPeliculas_json(lista_peliculas)