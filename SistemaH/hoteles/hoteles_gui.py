import tkinter as tk
from tkinter import messagebox
from .gestion_reservas_hotel import (guardar_reservas as guardar_hoteles, cargar_reservas as cargar_hoteles,buscar_reserva, eliminar_reserva)
from hoteles.reserva_hotel import ReservaHotel

class GestionHotelesGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Gestión de Reservas de Hoteles")

        self.hoteles = cargar_hoteles("data/hoteles.json")

        self.create_widgets()

    def create_widgets(self):
        # Crear Widgets
        self.label = tk.Label(self.master, text="Gestión de Reservas de Hoteles", font=("Arial", 14))
        self.label.pack(pady=10)

        self.add_reserva_button = tk.Button(self.master, text="Añadir Reserva", command=self.add_reserva)
        self.add_reserva_button.pack(pady=5)

        self.search_reserva_button = tk.Button(self.master, text="Buscar Reserva", command=self.search_reserva)
        self.search_reserva_button.pack(pady=5)

        self.delete_reserva_button = tk.Button(self.master, text="Eliminar Reserva", command=self.delete_reserva)
        self.delete_reserva_button.pack(pady=5)

        self.view_all_button = tk.Button(self.master, text="Ver Todas las Reservas", command=self.view_all)
        self.view_all_button.pack(pady=5)

    def add_reserva(self):
        # Crear ventana para añadir una reserva
        self.add_window = tk.Toplevel(self.master)
        self.add_window.title("Añadir Reserva")

        tk.Label(self.add_window, text="Código de Reserva:").pack(pady=5)
        self.codigo_reserva_entry = tk.Entry(self.add_window)
        self.codigo_reserva_entry.pack(pady=5)

        tk.Label(self.add_window, text="Cliente:").pack(pady=5)
        self.cliente_entry = tk.Entry(self.add_window)
        self.cliente_entry.pack(pady=5)

        tk.Label(self.add_window, text="Hotel:").pack(pady=5)
        self.hotel_entry = tk.Entry(self.add_window)
        self.hotel_entry.pack(pady=5)

        tk.Label(self.add_window, text="Fecha de Reserva:").pack(pady=5)
        self.fecha_reserva_entry = tk.Entry(self.add_window)
        self.fecha_reserva_entry.pack(pady=5)

        tk.Label(self.add_window, text="Fecha de Check-in:").pack(pady=5)
        self.fecha_checkin_entry = tk.Entry(self.add_window)
        self.fecha_checkin_entry.pack(pady=5)

        tk.Label(self.add_window, text="Fecha de Check-out:").pack(pady=5)
        self.fecha_checkout_entry = tk.Entry(self.add_window)
        self.fecha_checkout_entry.pack(pady=5)

        tk.Button(self.add_window, text="Guardar", command=self.save_reserva).pack(pady=10)

    def save_reserva(self):
        codigo_reserva = self.codigo_reserva_entry.get()
        cliente = self.cliente_entry.get()
        hotel = self.hotel_entry.get()
        fecha_reserva = self.fecha_reserva_entry.get()
        fecha_checkin = self.fecha_checkin_entry.get()
        fecha_checkout = self.fecha_checkout_entry.get()

        if (codigo_reserva and cliente and hotel and fecha_reserva and
            fecha_checkin and fecha_checkout):
            reserva = ReservaHotel(codigo_reserva, cliente, hotel, fecha_reserva, fecha_checkin, fecha_checkout)
            self.hoteles.append(reserva)
            guardar_hoteles(self.hoteles, "data/hoteles.json")
            self.add_window.destroy()
            messagebox.showinfo("Éxito", "Reserva añadida correctamente.")
        else:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")

    def search_reserva(self):
        # Crear ventana para buscar una reserva
        self.search_window = tk.Toplevel(self.master)
        self.search_window.title("Buscar Reserva")

        tk.Label(self.search_window, text="Código de Reserva:").pack(pady=5)
        self.codigo_reserva_search_entry = tk.Entry(self.search_window)
        self.codigo_reserva_search_entry.pack(pady=5)

        tk.Button(self.search_window, text="Buscar", command=self.find_reserva).pack(pady=10)

    def find_reserva(self):
        codigo_reserva = self.codigo_reserva_search_entry.get()
        reserva = buscar_reserva(self.hoteles, codigo_reserva)

        if reserva:
            messagebox.showinfo("Resultado", reserva.mostrar_info())
        else:
            messagebox.showwarning("No Encontrado", "Reserva no encontrada.")

    def delete_reserva(self):
        # Crear ventana para eliminar una reserva
        self.delete_window = tk.Toplevel(self.master)
        self.delete_window.title("Eliminar Reserva")

        tk.Label(self.delete_window, text="Código de Reserva:").pack(pady=5)
        self.codigo_reserva_delete_entry = tk.Entry(self.delete_window)
        self.codigo_reserva_delete_entry.pack(pady=5)

        tk.Button(self.delete_window, text="Eliminar", command=self.remove_reserva).pack(pady=10)

    def remove_reserva(self):
        codigo_reserva = self.codigo_reserva_delete_entry.get()
        if eliminar_reserva(self.hoteles, codigo_reserva):
            guardar_hoteles(self.hoteles, "data/hoteles.json")
            self.delete_window.destroy()
            messagebox.showinfo("Éxito", "Reserva eliminada correctamente.")
        else:
            messagebox.showwarning("No Encontrado", "Reserva no encontrada.")

    def view_all(self):
        # Crear ventana para mostrar todas las reservas
        self.view_window = tk.Toplevel(self.master)
        self.view_window.title("Ver Todas las Reservas")

        for reserva in self.hoteles:
            tk.Label(self.view_window, text=reserva.mostrar_info()).pack(pady=5)

def main(master):
    app = GestionHotelesGUI(master)

if __name__ == "__main__":
    pass
