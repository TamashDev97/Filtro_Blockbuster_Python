### Importaciones ###

import os

### Funciones para mejorar la visualización de los menus ###

def limpiar_pantalla():
    os.system('clear' if os.name == 'posix' else 'cls') 


def validar_opcion(enunciando,inferior,superior):
    while True:
        try:
            opcion =int(input(enunciando))
            if opcion>=inferior and opcion<=superior:
                return opcion
            else:
                print(f"Opción no está entre el intervalo de ({inferior}-{superior})")
        except ValueError:
            print("Por favor, introduce un número válido. ")

def pausa():
    input("Clic cualquier teclas [continuar]: ")


def validar_entrada_numerica(enunciado):
    while True:
        try:
            numero = int(input(enunciado))
            if numero > 0:
                return numero
            else:
                print("Por favor, introduce un número positivo.")
        except ValueError:
            print("Por favor, introduce un número válido.")


def validar_entrada_texto(enunciado):
    while True:
        texto = input(enunciado)
        if texto:
            return texto
        else:
            print("Por favor, introduce un valor válido.")