import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from vuelos.reserva_vuelo import ReservaVuelo
from vuelos.gestion_reservas_vuelo import (guardar_reservas, cargar_reservas, 
                                           buscar_reserva, eliminar_reserva)

# Clase para gestionar la interfaz gráfica de reservas de vuelos
class GestionVuelosGUI:
    def __init__(self, master):
        """
        Inicializa la interfaz gráfica.
        
        Args:
        master (tk.Tk): La ventana principal de Tkinter.
        """
        self.master = master
        self.master.title("Gestión de Reservas de Vuelos")
        self.create_widgets()
        self.reservas = cargar_reservas("data/reservas_vuelo.json")

    def create_widgets(self):
        """
        Crea y organiza los widgets en la ventana principal.
        """
        tk.Label(self.master, text="Gestión de Reservas de Vuelos", font=("Arial", 16)).pack(pady=10)
        
        tk.Button(self.master, text="Añadir Reserva", command=self.add_reserva).pack(pady=5)
        tk.Button(self.master, text="Buscar Reserva", command=self.search_reserva).pack(pady=5)
        tk.Button(self.master, text="Actualizar Reserva", command=self.update_reserva).pack(pady=5)
        tk.Button(self.master, text="Eliminar Reserva", command=self.delete_reserva).pack(pady=5)
        tk.Button(self.master, text="Ver Todas las Reservas", command=self.view_all).pack(pady=5)
        tk.Button(self.master, text="Salir", command=self.master.quit).pack(pady=10)

    def add_reserva(self):
        """
        Abre una ventana para añadir una nueva reserva.
        """
        self.add_reserva_window = tk.Toplevel(self.master)
        self.add_reserva_window.title("Añadir Reserva")

        # Campos para ingresar datos de la reserva
        tk.Label(self.add_reserva_window, text="Código de Reserva:").pack(pady=5)
        self.codigo_reserva_entry = tk.Entry(self.add_reserva_window)
        self.codigo_reserva_entry.pack(pady=5)

        tk.Label(self.add_reserva_window, text="Cliente:").pack(pady=5)
        self.cliente_entry = tk.Entry(self.add_reserva_window)
        self.cliente_entry.pack(pady=5)

        tk.Label(self.add_reserva_window, text="Vuelo:").pack(pady=5)
        self.vuelo_entry = tk.Entry(self.add_reserva_window)
        self.vuelo_entry.pack(pady=5)

        tk.Label(self.add_reserva_window, text="Fecha de Reserva (YYYY-MM-DD):").pack(pady=5)
        self.fecha_reserva_entry = tk.Entry(self.add_reserva_window)
        self.fecha_reserva_entry.pack(pady=5)

        tk.Label(self.add_reserva_window, text="Fecha de Salida (YYYY-MM-DD):").pack(pady=5)
        self.fecha_salida_entry = tk.Entry(self.add_reserva_window)
        self.fecha_salida_entry.pack(pady=5)

        tk.Label(self.add_reserva_window, text="Fecha de Llegada (YYYY-MM-DD):").pack(pady=5)
        self.fecha_llegada_entry = tk.Entry(self.add_reserva_window)
        self.fecha_llegada_entry.pack(pady=5)

        tk.Button(self.add_reserva_window, text="Guardar", command=self.save_reserva).pack(pady=10)

    def save_reserva(self):
        """
        Guarda la nueva reserva en la lista y en el archivo.
        """
        codigo_reserva = self.codigo_reserva_entry.get()
        cliente = self.cliente_entry.get()
        vuelo = self.vuelo_entry.get()
        fecha_reserva_str = self.fecha_reserva_entry.get()
        fecha_salida_str = self.fecha_salida_entry.get()
        fecha_llegada_str = self.fecha_llegada_entry.get()

        try:
            fecha_reserva = datetime.strptime(fecha_reserva_str, "%Y-%m-%d").date()
            fecha_salida = datetime.strptime(fecha_salida_str, "%Y-%m-%d").date()
            fecha_llegada = datetime.strptime(fecha_llegada_str, "%Y-%m-%d").date()
        except ValueError:
            messagebox.showerror("Error", "Formato de fecha inválido. Use YYYY-MM-DD.")
            return

        reserva = ReservaVuelo(codigo_reserva, cliente, vuelo, fecha_reserva, fecha_salida, fecha_llegada)
        self.reservas.append(reserva)
        guardar_reservas(self.reservas, "data/reservas_vuelo.json")
        messagebox.showinfo("Éxito", "Reserva añadida correctamente.")
        self.add_reserva_window.destroy()

    def search_reserva(self):
        """
        Abre una ventana para buscar una reserva existente.
        """
        self.search_reserva_window = tk.Toplevel(self.master)
        self.search_reserva_window.title("Buscar Reserva")

        tk.Label(self.search_reserva_window, text="Código de Reserva:").pack(pady=5)
        self.search_codigo_entry = tk.Entry(self.search_reserva_window)
        self.search_codigo_entry.pack(pady=5)

        tk.Button(self.search_reserva_window, text="Buscar", command=self.find_reserva).pack(pady=10)

    def find_reserva(self):
        """
        Busca y muestra la reserva con el código ingresado.
        """
        codigo_reserva = self.search_codigo_entry.get()
        reserva = buscar_reserva(self.reservas, codigo_reserva)
        if reserva:
            info = reserva.mostrar_info()
            messagebox.showinfo("Reserva Encontrada", info)
        else:
            messagebox.showerror("Error", "Reserva no encontrada.")
        self.search_reserva_window.destroy()

    def update_reserva(self):
        """
        Abre una ventana para actualizar una reserva existente.
        """
        self.update_reserva_window = tk.Toplevel(self.master)
        self.update_reserva_window.title("Actualizar Reserva")

        tk.Label(self.update_reserva_window, text="Código de Reserva:").pack(pady=5)
        self.update_codigo_entry = tk.Entry(self.update_reserva_window)
        self.update_codigo_entry.pack(pady=5)

        tk.Button(self.update_reserva_window, text="Buscar", command=self.load_reserva_for_update).pack(pady=10)

    def load_reserva_for_update(self):
        """
        Carga la reserva para su actualización.
        """
        codigo_reserva = self.update_codigo_entry.get()
        self.reserva = buscar_reserva(self.reservas, codigo_reserva)
        if self.reserva:
            self.show_update_fields()
        else:
            messagebox.showerror("Error", "Reserva no encontrada.")
            self.update_reserva_window.destroy()

    def show_update_fields(self):
        """
        Muestra los campos para actualizar los datos de la reserva.
        """
        tk.Label(self.update_reserva_window, text="Nuevo Cliente (dejar vacío para mantener):").pack(pady=5)
        self.update_cliente_entry = tk.Entry(self.update_reserva_window)
        self.update_cliente_entry.pack(pady=5)

        tk.Label(self.update_reserva_window, text="Nuevo Vuelo (dejar vacío para mantener):").pack(pady=5)
        self.update_vuelo_entry = tk.Entry(self.update_reserva_window)
        self.update_vuelo_entry.pack(pady=5)

        tk.Label(self.update_reserva_window, text="Nueva Fecha de Reserva (YYYY-MM-DD, dejar vacío para mantener):").pack(pady=5)
        self.update_fecha_reserva_entry = tk.Entry(self.update_reserva_window)
        self.update_fecha_reserva_entry.pack(pady=5)

        tk.Label(self.update_reserva_window, text="Nueva Fecha de Salida (YYYY-MM-DD, dejar vacío para mantener):").pack(pady=5)
        self.update_fecha_salida_entry = tk.Entry(self.update_reserva_window)
        self.update_fecha_salida_entry.pack(pady=5)

        tk.Label(self.update_reserva_window, text="Nueva Fecha de Llegada (YYYY-MM-DD, dejar vacío para mantener):").pack(pady=5)
        self.update_fecha_llegada_entry = tk.Entry(self.update_reserva_window)
        self.update_fecha_llegada_entry.pack(pady=5)

        tk.Button(self.update_reserva_window, text="Actualizar", command=self.apply_update).pack(pady=10)

    def apply_update(self):
        """
        Aplica los cambios a la reserva existente.
        """
        nuevo_cliente = self.update_cliente_entry.get() or None
        nuevo_vuelo = self.update_vuelo_entry.get() or None
        nueva_fecha_reserva_str = self.update_fecha_reserva_entry.get() or None
        nueva_fecha_salida_str = self.update_fecha_salida_entry.get() or None
        nueva_fecha_llegada_str = self.update_fecha_llegada_entry.get() or None

        try:
            nueva_fecha_reserva = datetime.strptime(nueva_fecha_reserva_str, "%Y-%m-%d").date() if nueva_fecha_reserva_str else None
            nueva_fecha_salida = datetime.strptime(nueva_fecha_salida_str, "%Y-%m-%d").date() if nueva_fecha_salida_str else None
            nueva_fecha_llegada = datetime.strptime(nueva_fecha_llegada_str, "%Y-%m-%d").date() if nueva_fecha_llegada_str else None
        except ValueError:
            messagebox.showerror("Error", "Formato de fecha inválido. Use YYYY-MM-DD.")
            return

        # Actualizar los atributos si se proporcionan nuevos valores
        if nuevo_cliente is not None:
            self.reserva.cliente = nuevo_cliente
        if nuevo_vuelo is not None:
            self.reserva.vuelo = nuevo_vuelo
        if nueva_fecha_reserva is not None:
            self.reserva.fecha_reserva = nueva_fecha_reserva
        if nueva_fecha_salida is not None:
            self.reserva.fecha_salida = nueva_fecha_salida
        if nueva_fecha_llegada is not None:
            self.reserva.fecha_llegada = nueva_fecha_llegada

        guardar_reservas(self.reservas, "data/reservas_vuelo.json")
        messagebox.showinfo("Éxito", "Reserva actualizada correctamente.")
        self.update_reserva_window.destroy()

    def delete_reserva(self):
        """
        Abre una ventana para eliminar una reserva existente.
        """
        self.delete_reserva_window = tk.Toplevel(self.master)
        self.delete_reserva_window.title("Eliminar Reserva")

        tk.Label(self.delete_reserva_window, text="Código de Reserva:").pack(pady=5)
        self.delete_codigo_entry = tk.Entry(self.delete_reserva_window)
        self.delete_codigo_entry.pack(pady=5)

        tk.Button(self.delete_reserva_window, text="Eliminar", command=self.remove_reserva).pack(pady=10)

    def remove_reserva(self):
        """
        Elimina la reserva con el código ingresado.
        """
        codigo_reserva = self.delete_codigo_entry.get()
        if eliminar_reserva(self.reservas, codigo_reserva):
            guardar_reservas(self.reservas, "data/reservas_vuelo.json")
            messagebox.showinfo("Éxito", "Reserva eliminada correctamente.")
        else:
            messagebox.showerror("Error", "Reserva no encontrada.")
        self.delete_reserva_window.destroy()

    def view_all(self):
        """
        Muestra todas las reservas en un mensaje.
        """
        all_reservas = "\n".join(reserva.mostrar_info() for reserva in self.reservas)
        if all_reservas:
            messagebox.showinfo("Todas las Reservas", all_reservas)
        else:
            messagebox.showinfo("Todas las Reservas", "No hay reservas registradas.")

# Función principal para iniciar la interfaz gráfica
def main():
    """
    Función principal para iniciar la interfaz gráfica.
    """
    root = tk.Tk()
    app = GestionVuelosGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()

