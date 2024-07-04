import time
from opciones import seleccionar_opcion

def menu():
    print('Bienvenido a "Autos Locos"')
    print("1) Agregar un nuevo auto al inventario")
    print("2) Eliminar un auto del inventario por ID")
    print("3) Mostrar un auto del inventario por ID")
    print("4) Mostrar el listado de todos los IDs y la marca/modelo del auto que corresponde a ese ID, ordenado de forma creciente el ID")
    print("5) Mostrar el listado de todos los IDs y el modelo y precio, ordenado de forma creciente el precio")
    print("6) Informar cuantos autos hay cargados en el inventario")
    print("7) Marcar un auto como reservado por ID")
    print("8) Mostrar el listado de todos los IDs y modelos que hayan sido marcados como reservados")
    print("9) Mostrar el Inventario")
    print("0) Terminar")


def volver_menu():
    print("Volviendo al menu principal...")
    print()
    time.sleep(1)
    seleccionar_opcion()


