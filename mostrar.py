import time
from variables import listado_de_autos
from opciones import seleccionar_opcion
from menu import volver_menu


def mostrar_inventario():
    print("IVENTARIO: ")
    if not listado_de_autos:
        print("El Inventario esta Vacio!")
        print("Volviendo al menu principal...")
        print()
        time.sleep(1)
        seleccionar_opcion()
    else:
        for id, detalles in listado_de_autos.items():
            print("-----------------------")
            print(f"ID: {id}")
            for clave, valor in detalles.items():
                print(f"{clave}: {valor}")
    print()
    volver = input("Presione '0' para volver al menu: ")
    if volver == "0":
        volver_menu()



def mostrar_auto():
    id_mostrar = int(input("Ingrese el ID del auto (0 para volver al menu): "))
    if id_mostrar == 0:
        volver_menu()

    elif id_mostrar in listado_de_autos:
        print(f"ID: {id_mostrar}")
        print(f"Marca: {listado_de_autos[id_mostrar]["marca"]}")
        print(f"Modelo: {listado_de_autos[id_mostrar]["modelo"]}")
        print(f"Año: {listado_de_autos[id_mostrar]["año"]}")
        print(f"Precio: ${listado_de_autos[id_mostrar]["precio"]}")
        print(f"Reservado: {listado_de_autos[id_mostrar]["reservado"]}")
        print()
        ver_otro = input("Desea ver otro ID? (si/no): ")
        if ver_otro != "si":
            volver_menu()
        else:
            mostrar_auto()

    else:
        print(f"El ID {id_mostrar} no existe en el Inventario!")
        print()
        mostrar_auto()

#####################################################################################

def mostrar_todos():
    id_ordenado = sorted(listado_de_autos.items())
    #utilizo la funcion sorted para ordenar de forma creciente los elementos del diccionario por el valor de 'id' 

    #uso un for para iterar los id y los detalles de cada id dentro del diccionario
    for id, detalles in id_ordenado:
        #si marca y modelo estan en los detalles de cada id iterado en el for...
        if 'marca' in detalles and 'modelo' in detalles:
            #defino las variables marca y modelo, las cuales son las key de cada detalle
            marca = detalles['marca']
            modelo = detalles['modelo']
            print(f"ID: {id} - Marca: {marca} / Modelo: {modelo}")
    print()
    volver = input("Presione '0' para volver al menu: ")
    if volver == "0":
        volver_menu()



def mostrar_precios():
    precio_ordenado = sorted(listado_de_autos.items(), key=lambda x: x[1]['precio'])
    #utilizo la funcion sorted para ordenar y la funciona lambda para ordenar los elementos del diccionario por el valor de 'precio' 
    # en cada diccionario de auto (x[1] se refiere al valor del par clave-valor en el diccionario principal).
    for id, detalles in precio_ordenado:
        marca = detalles['marca']
        modelo = detalles['modelo']
        precio = detalles['precio']
        print(f"ID: {id} - Marca: {marca} / Modelo: {modelo} ($ {precio})")
    
    print()
    volver = input("Presione '0' para volver al menu: ")
    if volver == "0":
        volver_menu()


"""en la funcion mostrar_todos y mostrar_precios la diferencia esta en que en la primera uso solo la funcion sorted() para ordenar los ID's;
y en la segunda funcion, ademas de usar sorted(), le agreg0 una funcion lambda para ordenar por el valor que deseo (en este caso precio) dentro
de cada diccionario en el diccionario "madre" que es listado_de_autos
en la funcion lambda (x[1] se refiere al valor del par clave-valor en el diccionario principal)"""
#############################################################################################