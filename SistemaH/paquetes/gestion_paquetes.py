import json
from .paquete_turistico import PaqueteTuristico

def obtener_ruta_archivo_paquetes():
    return "data/paquetes.json"

def guardar_paquetes(paquetes, archivo):
    with open(archivo, 'w') as f:
        json.dump([paquete.__dict__ for paquete in paquetes], f, indent=4)

def cargar_paquetes(archivo):
    try:
        with open(archivo, 'r') as f:
            paquetes_data = json.load(f)
            return [PaqueteTuristico(**data) for data in paquetes_data]
    except FileNotFoundError:
        return []

def buscar_paquete(paquetes, nombre):
    for paquete in paquetes:
        if paquete.nombre == nombre:
            return paquete
    return None

def eliminar_paquete(paquetes, nombre):
    paquete = buscar_paquete(paquetes, nombre)
    if paquete:
        paquetes.remove(paquete)
        return True
    return False
