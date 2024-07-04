import time
from variables import listado_de_autos
from opciones import seleccionar_opcion
from menu import volver_menu



def contar_autos():
    if not listado_de_autos:
        print("El Inventario esta Vacio!")
        print("--------------------")
        print("Volviendo al menu principal...")
        print()
        time.sleep(1)
        seleccionar_opcion()
    else:
        cantidad_de_autos = len(listado_de_autos)
        print(f"Hay cargados {cantidad_de_autos} autos")

    print()
    volver = input("Presione '0' para volver al menu: ")
    if volver == "0":
        volver_menu()