import os
import tkinter as tk
from tkinter import messagebox
import json

class Cliente:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def actualizar_email(self, nuevo_email):
        self.email = nuevo_email

    def mostrar_info(self):
        return f"Cliente: {self.nombre}, Email: {self.email}"

    def to_dict(self):
        return {"nombre": self.nombre, "email": self.email}

    @staticmethod
    def from_dict(data):
        return Cliente(data['nombre'], data['email'])

def obtener_ruta_archivo_clientes():
    return os.path.join("data", "clientes.json")

def guardar_clientes(clientes):
    archivo = obtener_ruta_archivo_clientes()
    with open(archivo, 'w') as f:
        json.dump([cliente.to_dict() for cliente in clientes], f, indent=4)

def cargar_clientes():
    archivo = obtener_ruta_archivo_clientes()
    try:
        with open(archivo, 'r') as f:
            clientes_data = json.load(f)
            return [Cliente.from_dict(data) for data in clientes_data]
    except FileNotFoundError:
        return []

def buscar_cliente(clientes, criterio):
    for cliente in clientes:
        if cliente.nombre == criterio or cliente.email == criterio:
            return cliente
    return None

def eliminar_cliente(clientes, criterio):
    cliente = buscar_cliente(clientes, criterio)
    if cliente:
        clientes.remove(cliente)
        return True
    return False
