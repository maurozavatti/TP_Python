from menu import volver_menu
from variables import listado_de_autos


def reservar_auto():
    reservar = int(input("Ingrese el ID del auto a reservar (0 para volver al menu): "))
    #aca pongo el input como int, ya que en la funcion agregar autos, los IDs los pedi como int

    if reservar == 0:
        volver_menu()

    if reservar in listado_de_autos:      #aca no se usa .items() porque no es necesario buscar el par clave : valor
                                                           
        auto_reservado = listado_de_autos[reservar]  #esto es que la variable auto es igual al ID identificado ya dentro del dicc listado de autos, 
                                                    # osea que [reservar] es igual al ID que esta dentro del dicc , identificado por el condicional
                                                       
        if auto_reservado['reservado']: #esta la condicion True
             print(f'EL ID {reservar} ya esta reservado, no fue posible reservarlo')
        
        #(*) if auto.get('reservado',False):
            #print(f'EL ID {reservar} ya esta reservado, no fue posible reservarlo')

        else: #esta es la condicion False
            auto_reservado['reservado'] = True
            print(f'El ID {reservar} quedo reservado')
            continuar = input("Desea reservar otro auto? (si/no): ")
            if continuar != "si":
                volver_menu()
            else:
                reservar_auto()
    else:
        print('El ID ingresado no existe en el inventario!')
        print()

#(*) Si la clave 'reservado' existe en el diccionario auto, get() devolverá el valor correspondiente a esa clave.
#    Si la clave no existe, get() devolverá False porque ese es el valor por defecto que se especifica como segundo argumento (False).

############################################################################################

def mostrar_reservados():
    print("Los autos reservado son: ")
    print()

    for id, auto in listado_de_autos.items():
    #la variable "id" se refiere a acada id dentro del dict listado_de_autos    
    #la variable "auto" se refiere a cada clave dentro de cada id
        if auto['reservado']:
            #esto es si la condicion de la key dentro de auto es True...
            print(f"ID {id} - Marca: {auto['marca']} / Modelo: {auto['modelo']}")
        
    print()
    volver = input("Presione '0' para volver al menu: ")
    if volver == "0":
        volver_menu()