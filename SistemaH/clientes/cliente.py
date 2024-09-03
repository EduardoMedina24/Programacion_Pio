import os
import json

class Cliente:
    """
    Clase que representa a un cliente.

    Atributos:
    ----------
    nombre : str
        Nombre del cliente.
    email : str
        Correo electrónico del cliente.
    """

    def __init__(self, nombre, email):
        """
        Inicializa un objeto Cliente con su nombre y email.

        Parámetros:
        -----------
        nombre : str
            Nombre del cliente.
        email : str
            Correo electrónico del cliente.
        """
        self.nombre = nombre
        self.email = email

    def actualizar_email(self, nuevo_email):
        """
        Actualiza el correo electrónico del cliente.

        Parámetros:
        -----------
        nuevo_email : str
            Nuevo correo electrónico.
        """
        self.email = nuevo_email

    def mostrar_info(self):
        """
        Muestra la información del cliente.

        Retorna:
        --------
        str : Información del cliente en formato 'Cliente: nombre, Email: email'.
        """
        return f"Cliente: {self.nombre}, Email: {self.email}"

    def to_dict(self):
        """
        Convierte la información del cliente en un diccionario.

        Retorna:
        --------
        dict : Diccionario con el nombre y email del cliente.
        """
        return {"nombre": self.nombre, "email": self.email}

    @staticmethod
    def from_dict(data):
        """
        Crea un objeto Cliente a partir de un diccionario.

        Parámetros:
        -----------
        data : dict
            Diccionario con la información del cliente.

        Retorna:
        --------
        Cliente : Un objeto Cliente.
        """
        return Cliente(data['nombre'], data['email'])

def obtener_ruta_archivo_clientes():
    """
    Obtiene la ruta del archivo donde se guardan los datos de los clientes.

    Retorna:
    --------
    str : Ruta del archivo 'clientes.json'.
    """
    return os.path.join("data", "clientes.json")

def guardar_clientes(clientes):
    """
    Guarda la lista de clientes en un archivo JSON.

    Parámetros:
    -----------
    clientes : list
        Lista de objetos Cliente a guardar.
    """
    archivo = obtener_ruta_archivo_clientes()
    with open(archivo, 'w') as f:
        json.dump([cliente.to_dict() for cliente in clientes], f, indent=4)

def cargar_clientes():
    """
    Carga los clientes desde un archivo JSON.

    Retorna:
    --------
    list : Lista de objetos Cliente.
    """
    archivo = obtener_ruta_archivo_clientes()
    try:
        with open(archivo, 'r') as f:
            clientes_data = json.load(f)
            return [Cliente.from_dict(data) for data in clientes_data]
    except FileNotFoundError:
        return []

def buscar_cliente(clientes, criterio):
    """
    Busca un cliente en la lista por nombre o email.

    Parámetros:
    -----------
    clientes : list
        Lista de objetos Cliente.
    criterio : str
        Nombre o email del cliente a buscar.

    Retorna:
    --------
    Cliente or None : Cliente si se encuentra, de lo contrario, None.
    """
    for cliente in clientes:
        if cliente.nombre == criterio or cliente.email == criterio:
            return cliente
    return None

def eliminar_cliente(clientes, criterio):
    """
    Elimina un cliente de la lista basado en el nombre o email.

    Parámetros:
    -----------
    clientes : list
        Lista de objetos Cliente.
    criterio : str
        Nombre o email del cliente a eliminar.

    Retorna:
    --------
    bool : True si el cliente fue eliminado, False si no se encontró.
    """
    cliente = buscar_cliente(clientes, criterio)
    if cliente:
        clientes.remove(cliente)
        return True
    return False
