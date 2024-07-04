import time
from variables import listado_de_autos
from opciones import seleccionar_opcion
from menu import volver_menu
from mostrar import mostrar_inventario


def agregar_autos():
    print("Se va a agregar un auto")
    id = int(input("Ingrese el ID del auto: "))
    
    if id in listado_de_autos:
        sobrescribir = input("El ID ingresado ya esta dentro del inventario, desea sobrescribirlo? (si/no): ")
        if sobrescribir.lower() != "si":
            print("No se sobrescribe auto, volviendo al ingreso...")
            return #aca retorno nuevamente al principio de la funcion
        
    marca = input("Ingrese la marca del auto: ")
    modelo = input("Ingrese modelo del auto: ")
    año = int(input("Ingrese año de fabricacion: "))
    precio = float(input("Ingrese precio: $ "))
    reservado = False 
    
    datos_de_auto = {
        "marca" : marca,
        "modelo" : modelo,
        "año" : año,
        "precio" : precio,
        "reservado" : reservado
    }
    
    #agrego los datos del auto al id ingresado como key 
    listado_de_autos[id] = datos_de_auto

    print("El auto se agrego al inventario correctamente!")
    print()
    print("El Inventario es: ")
    #con un for voy mostrando como se va completrando el inventario de autos
    for id, detalles in listado_de_autos.items():
        print("--------------------------------")
        print(f"ID: {id}")
        for clave, valor in detalles.items():
            print(f"{clave}: {valor}")

    #defino bucle while para ingresar mas autos al inventario
    while True:
        agregar_mas = str(input("Desea ingresar otro auto? (si/no): "))
        if agregar_mas.lower() != "si":
            print("Volviendo al menu principal...")
            print()
            time.sleep(1) #volver al menu de las opciones 
            seleccionar_opcion()
            break
        else:
            agregar_autos()


def eliminar_auto():
    id_eliminar = int(input("Ingrese el ID del auto que desea eliminar (0 para volver al menu): "))
    if id_eliminar == "0":
        volver_menu()

    elif id_eliminar in listado_de_autos:
        listado_de_autos.pop(id_eliminar)
        print(f"Se elimino correctamente el ID {id_eliminar}")
        print()
        print("El inventario quedo: ")
        print()
        mostrar_inventario()

    else:
        print(f"El ID {id_eliminar} no existe en el Inventario, no se pudo eliminar")
        eliminar_auto()