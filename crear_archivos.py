from service_drive import obtener_servicio as SERVICE_DRIVE
from service_gmail import obtener_servicio as SERVICE_GMAIL
from tqdm import tqdm
from time import sleep

def tipos_archivos_creacion() -> None:
    """
    Tipos de archivos para crear
    """
    print("1) Crear un archivo PowerPoint\n"
          "2) Crear un archivo Word\n"
          "3) Crear un archivo Excel\n"
          "4) Crear un archivo Form\n"
          "5) Crear una carpeta\n"
          "6) Salir")

def elegir_extension(archivo_elegido: str) -> list:
    """
    Pre: Obtengo un tipo de archivo
    Post: Devuelve una lista con mimetype y su extension
    """
    mimeType = ''
    if int(archivo_elegido) == 1:
        mimeType = 'application/vnd.google-apps.presentation'
    elif int(archivo_elegido) == 2:
        mimeType = 'application/vnd.google-apps.document'
    elif int(archivo_elegido) == 3:
        mimeType = 'application/vnd.google-apps.spreadsheet'
    elif int(archivo_elegido) == 4:
        mimeType = 'application/vnd.google-apps.form'
    return mimeType


def crear_archivo_drive(tipo_archivo: str) -> None:
    """
    Pre: Necesita el mimetype del archivo y su nombre
    Post: Crea el archivo en drive
    """
    nombre_archivo = input("Ingrese el nombre del archivo: ")
    archivo_metadata = {
        'name': nombre_archivo,
        'mimeType': tipo_archivo
    }
    SERVICE_DRIVE().files().create(body = archivo_metadata, fields = 'id').execute()
    for i in tqdm(range(0, 100), desc ="Creando archivo"):
        sleep(.01)
    print("\nARCHIVO CREADO!!")

def crear_carpeta_drive() -> None:
    """
    Crea una carpeta en drive
    """
    nombre_carpeta = input("Ingrese el nombre de la carpeta: ")
    archivo_metadata = {
        'name': nombre_carpeta,
        'mimeType': 'application/vnd.google-apps.folder'
    }
    SERVICE_DRIVE().files().create(body = archivo_metadata, fields = 'id').execute()
    for i in tqdm(range(0, 100), desc ="Creando carpeta"):
        sleep(.01)
    print("\nCARPETA CREADA!!")


def creacion_archivos() -> None:
    """
    Elige el tipo de archivo que quiere crear
    """
    acceso = True
    while acceso:
        print("\n\t\t\t\tCREACION DE ARCHIVOS DRIVE\n")
        tipos_archivos_creacion()
        opcion = input("Que quieres crear: ")
        while not opcion.isnumeric() or int(opcion) < 1 or int(opcion) > 6:
            opcion = input("Ingrese una opcion correcta: ")
        extension = elegir_extension(opcion)
        if 1 <= int(opcion) <= 4:
            crear_archivo_drive(extension)
        elif int(opcion) == 5:
            crear_carpeta_drive()
        elif int(opcion) == 6:
            acceso = False