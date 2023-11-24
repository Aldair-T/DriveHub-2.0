from service_drive import obtener_servicio as SERVICE_DRIVE
from service_gmail import obtener_servicio as SERVICE_GMAIL
from googleapiclient.http import MediaFileUpload
from listar_archivos import repo_local, buscar_id_carpeta, listar_archivos_local
import os
import pathlib
import mimetypes
from tqdm import tqdm
from time import sleep

def subir_a_unidad(nombre_archivo: str, ruta_archivo: str, tipo_archivo: str) -> None:
    """
    Pre: Necesitamos el nombre_archivo del nuevo archivo, la ruta a este, y su mimetype
    Post: Subimos el archivo a drive
    """
    file_metadata = {'name': nombre_archivo, 'mimeType': tipo_archivo}
    media = MediaFileUpload(ruta_archivo, mimetype = tipo_archivo)
    SERVICE_DRIVE().files().create(body = file_metadata,
                                   media_body = media,
                                   fields = 'id').execute()
    for i in tqdm(range(0, 100), desc ="Subiendo archivo"):
        sleep(.01)
    print("\nSE SUBIO EL ARCHIVO CON EXITO!!")


def subir_a_carpeta_especifica(nombre_archivo: str, ruta_archivo: str, tipo_archivo: str) -> None:
    """
    Pre: Necesitamos el nombre_archivo del archivo, el id de la carpeta, la ruta al archivo y su mimetype
    Post: Si existe la carpeta, subimos el archivo
    """
    nombre_carpeta = input("Ingrese el nombre de una carpeta o 0 para volver: ")
    id = buscar_id_carpeta(nombre_carpeta)
    while id == "" and nombre_carpeta != "0":
        print("\nEsa carpeta no existe!!\n")
        nombre_carpeta = input("Ingrese el nombre de una carpeta o 0 para volver: ")
        id = buscar_id_carpeta(nombre_carpeta) 

    if id != "":
        file_metadata = {'name': nombre_archivo, 'mimeType': tipo_archivo, 'parents': [id]}
        media = MediaFileUpload(ruta_archivo, mimetype = tipo_archivo)
        SERVICE_DRIVE().files().create(body = file_metadata,
                                       media_body = media,
                                       fields = 'id').execute()
        for i in tqdm(range(0, 100), desc ="Subiendo archivo"):
            sleep(.01)
        print("\nSE SUBIO EL ARCHIVO CON EXITO!!")



def elegir_lugar_subida(nombre_archivo: str, ruta_archivo: str, tipo_archivo: str) -> None:
    """
    Pre: Necesitamos la ruta al archivo y su mimetype
    Post: Ingresa unas opciones para después subir el archivo
    """
    respuesta = input("\nDeseas guardar en una carpeta especifica? s/n: ")
    while respuesta != "s" and respuesta != "n":
        respuesta = input("Deseas guardar en una carpeta especifica? s/n: ")
    if respuesta == "s":
        subir_a_carpeta_especifica(nombre_archivo, ruta_archivo, tipo_archivo)
    elif respuesta == "n":
        subir_a_unidad(nombre_archivo, ruta_archivo, tipo_archivo)


def mimetype_archivo(archivo:str) -> str:
    tipo = mimetypes.guess_type(archivo)
    if tipo[0] == None:
        print("Este archivo no se puede subir")
    return tipo[0]  



def subir_archivo() -> None:
    print("\n\t\t\t\tCREACION DE ARCHIVOS DRIVE\n")
    listar_archivos_local(os.getcwd())
    acceso = True
    nombre_archivo = input("Ingrese el nombre_archivo del archivo a subir: ")
    while os.path.isfile(pathlib.Path(os.getcwd(),nombre_archivo)) == False and acceso == True:
        nombre_archivo = input("Ingrese un archivo existente o 0 para salir: ")
        if nombre_archivo == "0":
            acceso = False

    ruta = pathlib.Path(os.getcwd(),nombre_archivo)
    if os.path.isfile(ruta):
        tipo_archivo = mimetype_archivo(nombre_archivo)
        if tipo_archivo != None:
            elegir_lugar_subida(nombre_archivo, ruta, tipo_archivo)
            