
from agregar_eliminar import agregar_autos as agregar, eliminar_auto as eliminar_auto
from mostrar import mostrar_auto as mostrar_auto, mostrar_inventario as mostrar_inventario, mostrar_todos as mostrar_todos, mostrar_precios as mostrar_precios
from contar_autos import contar_autos as contar
from reservar import reservar_auto as reservar, mostrar_reservados as mostrar_reservados
from menu import menu as menu, volver_menu as volver_menu


def seleccionar_opcion():
    menu
    opcion = input("Seleccione una opcion: ")
    print()
    while True:
        if opcion == "1":
            agregar
            break
        elif opcion == "2":
            eliminar_auto
            break
        elif opcion == "3":
            mostrar_auto
        elif opcion == "4":
            mostrar_todos
        elif opcion == "5":
            mostrar_precios
        elif opcion == "6":
            contar
        elif opcion == "7":
            reservar
        elif opcion == "8":
            mostrar_reservados
        elif opcion == "9":
            mostrar_inventario
            volver_menu
        elif opcion == "0":
            print("Hasta Luego!")
            quit()
        else:
            print("La opcion ingresada no corresponde a una del menu")
            seleccionar_opcion()