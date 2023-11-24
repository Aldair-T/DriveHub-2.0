from service_drive import obtener_servicio as SERVICE_DRIVE
from service_gmail import obtener_servicio as SERVICE_GMAIL
from tabulate import tabulate
import os, pathlib


def opciones() -> None:
    """
    Tipos de repositorios, local o remoto
    """
    print("1) Archivos locales\n"
          "2) Archivos remotos\n"
          "3) Salir")



def buscar_id_carpeta(nombre_carpeta) -> str:
    """
    Busca el id de la carpeta ingresada
    pre: nombre de la carpeta a buscar
    post: devuelve el id de la carpeta
    """
    id = ""
    respuesta = SERVICE_DRIVE().files().list(q= "mimeType='application/vnd.google-apps.folder'" and f"name='{nombre_carpeta}'", fields="files(id, name, mimeType)").execute()
    for valor in respuesta.values():
        for i in valor:
                id = i["id"]
    return id



def buscar_carpeta_drive() -> None:
    """
    Busca y lista una carpeta de DRIVE si existe
    """
    nombre_carpeta = input("Ingrese el nombre de la carpeta:")
    print("\n")
    id = buscar_id_carpeta(nombre_carpeta)
    if id != "":
        respuesta = SERVICE_DRIVE().files().list(q= f"parents = '{id}'", fields="files(id, name, mimeType)").execute()
        listar_archivos_drive(respuesta)
    else:
        print("No se encontro la carpeta")



def listar_archivos_drive(archivos) -> None:
    """
    Lista los archivos del parametro pasado
    pre: archivos a listar
    """
    if not archivos:
        print('No files found.')
    else:
        rows = []
        for item in archivos.values():
            for documento in item:
                id = documento["id"]
                name = documento["name"]
                mime_type = documento["mimeType"]
                rows.append((id, name, mime_type))
        print("Files:")
        # convert to a human readable table
        table = tabulate(rows, headers=["ID", "Name", "Type"])
        print(table)



def repo_remoto() -> None:
    """
    Listamos todas los archivos y carpetas de drive
    """
    print("\nREPOSITORIO REMOTO:\n")
    acceso = True
    respuesta = SERVICE_DRIVE().files().list(q="trashed=false",fields="files(id, name, mimeType)").execute()
    listar_archivos_drive(respuesta)
    while acceso:
        seguir = input("\nQueres buscar alguna carpeta? s/n: ")
        if seguir == "s":
            buscar_carpeta_drive()
        elif seguir == "n":
            acceso = False
        else:
            print("Ingrese una respuesta correcta")
                           


def volver(ruta) -> None:
    """
    Vuelve un paso atras de la ruta pasada como parametro
    pre: ruta de la carpeta
    post: ruta de la carpeta con un paso atras
    """
    if ruta != pathlib.Path.home():
        ruta = ruta.parent
        listar_archivos_local(ruta)
    else:
        print("Esta es la carpeta raiz")
    return ruta



def buscar_carpeta_local(ruta) -> None:
    """
    Busca y lista una carpeta del DIRECTORIO si existe
    pre: ruta anterior
    post: ruta con la carpeta buscada 
    """
    carpeta = input("Ingrese nombre de la carpeta: ")
    ruta = pathlib.Path(ruta, carpeta)
    if os.path.isdir(ruta):
        listar_archivos_local(ruta)
    else:
        print("La carpeta no existe o es un archivo")
        ruta = ruta.parent
        buscar_carpeta_local(ruta)
    return ruta



def listar_archivos_local(ruta) -> None:
    """
    Funcion itera y lista los archivos
    pre: ruta a listar
    """
    print("\n")
    for archivo in os.listdir(ruta):
        print(f"- {archivo}")    



def repo_local() -> None:
    """
    Lista los archivos de la ruta base
    """
    print("\nREPOSITORIO LOCAL:")
    acceso = True
    ruta = pathlib.Path.home()
    listar_archivos_local(ruta)
    while acceso:
        print("\n1)Buscar carpeta\n2)Volver\n3)Salir\n")
        opcion = input("Ingrese una opcion: ")
        while not opcion.isnumeric() or int(opcion) < 1 or int(opcion) > 3:
            opcion = input("Ingrese una opcion correcta: ")
        if int(opcion) == 1:
            ruta = buscar_carpeta_local(ruta)
        elif int(opcion) == 2:
            ruta = volver(ruta)
        elif int(opcion) == 3:
            acceso = False
    return ruta



def listar_archivos() -> None:
    """
    Elige si lista el repositorio local o remoto
    """
    acceso = True
    while acceso:
        print("\n\t\t\t\t LISTAR ARCHIVOS\n")
        opciones()
        opcion = input("Elija una opcion: ")
        while not opcion.isnumeric() or int(opcion) < 1 or int(opcion) > 3:
            opcion = input("Ingrese una opcion correcta: ")
        if int(opcion) == 1:
            repo_local()
        elif int(opcion) == 2:
            repo_remoto()
        elif int(opcion) == 3:
            acceso = False