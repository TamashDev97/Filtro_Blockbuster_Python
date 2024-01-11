from commons.menus import menu_peliculas, menu_principal, gestion_peliculas
from commons.utils import limpiar_pantalla, pausa
from businness.peliculas import *
from businness.gestion_catalogo import *

def peliculas():
    limpiar_pantalla()
    op = menu_peliculas()
    if op == 1:
        listar_peliculas()
        pausa()
    elif op == 2:
        buscar_pelicula_nombre()
        pausa()

def gestion_catalogo():
    limpiar_pantalla()
    op = gestion_peliculas()
    if op == 1:
        print("Agregar pelicula")
        pausa()
    elif op == 2:
        print("Modificar pelicula")
        pausa()
    elif op == 3:
        print("Eliminar pelicula")
        pausa()

#start
while True: 
   limpiar_pantalla()
   op = menu_principal()
   if  op == 1:
       peliculas()
   elif op == 2:
       gestion_catalogo()
   elif op == 3:
       print("Gracias por usar el sistema")
       break