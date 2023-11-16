from service_drive import obtener_servicio as SERVICE_DRIVE
from service_gmail import obtener_servicio as SERVICE_GMAIL
from listar_archivos import *
from crear_archivos import *

def menu() -> None:
    """
    Print del menu principal del programa
    """
    print("\n1) Listar archivos\n"
          "2) Crear un archivo\n"
          "3) Subir un archivo\n"
          "4) Descargar un archivo\n"
          "5) Sincronizar\n"
          "6) Genera carpeta de una evaluacion\n"
          "7) Actualizar entregas de alumnos via mail\n"
          "8) Salir")
    


def opcion_valida(opcion: str) -> int:
    """
    Verificamos q la opcion sea correcta
    """
    while not opcion.isnumeric() or int(opcion) < 1 or int(opcion) > 8:
        opcion = input("Ingrese una opcion correcta: ")
    opcion = int(opcion)
    return opcion



def main() -> None:
    """
    Menu principal
    """
    acceso = True
    while acceso:
        print("\n\n\t\t\t\t BIENVENIDOS A DRIVEHUB \n")
        menu()
        opcion = input("Ingrese una opcion: ")
        opcion = opcion_valida(opcion)
        if opcion == 1:
            listar_archivos()
        elif opcion == 2:
            creacion_archivos()
        elif opcion == 3:
            pass
            #subir_archivos()
        elif opcion == 4:
            pass
            #ingresar_carpeta_descarga()
        elif opcion == 5:
            pass
            #sincronizar()
        elif opcion == 6:
            pass
            #carpetas_encontradas()
        elif opcion == 7:
            pass
            #enviar_mensaje()
        elif opcion == 8:
            acceso = False


main()