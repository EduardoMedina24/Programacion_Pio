import json
from vuelos.reserva_vuelo import ReservaVuelo



def guardar_reservas(reservas, archivo):
    try:
        with open(archivo, 'w') as f:
            json.dump([reserva.to_dict() for reserva in reservas], f, indent=4)
    except IOError as e:
        print(f"Error al guardar el archivo: {e}")


def cargar_reservas(archivo):
    try:
        with open(archivo, 'r') as f:
            reservas_data = json.load(f)
            return [ReservaVuelo(**data) for data in reservas_data]
    except FileNotFoundError:
        print(f"Archivo no encontrado: {archivo}")
        return []
    except json.JSONDecodeError as e:
        print(f"Error al decodificar JSON: {e}")
        return []
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return []

def buscar_reserva(reservas, codigo_reserva):
    for reserva in reservas:
        if reserva.codigo_reserva == codigo_reserva:
            return reserva
    return None

def eliminar_reserva(reservas, codigo_reserva):
    reserva = buscar_reserva(reservas, codigo_reserva)
    if reserva:
        reservas.remove(reserva)
        return True
    return False
    


def to_dict(self):
    return {
        "codigo_reserva": self.codigo_reserva,
        "cliente": self.cliente,
        "vuelo": self.vuelo,
        "fecha_reserva": self.fecha_reserva.strftime('%Y-%m-%d'),
        "fecha_salida": self.fecha_salida.strftime('%Y-%m-%d'),
        "fecha_llegada": self.fecha_llegada.strftime('%Y-%m-%d')
        }
