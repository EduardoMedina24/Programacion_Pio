import tkinter as tk
from tkinter import messagebox

from paquetes.paquete_turistico import PaqueteTuristico
from paquetes.gestion_paquetes import guardar_paquetes, cargar_paquetes, buscar_paquete, eliminar_paquete

class GestionPaquetesGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Gestión de Paquetes Turísticos")

        self.paquetes = cargar_paquetes("data/paquetes.json")

        self.create_widgets()

    def create_widgets(self):
        # Crear Widgets
        self.label = tk.Label(self.master, text="Gestión de Paquetes Turísticos", font=("Arial", 14))
        self.label.pack(pady=10)

        self.add_paquete_button = tk.Button(self.master, text="Añadir Paquete", command=self.add_paquete)
        self.add_paquete_button.pack(pady=5)

        self.search_paquete_button = tk.Button(self.master, text="Buscar Paquete", command=self.search_paquete)
        self.search_paquete_button.pack(pady=5)

        self.delete_paquete_button = tk.Button(self.master, text="Eliminar Paquete", command=self.delete_paquete)
        self.delete_paquete_button.pack(pady=5)

        self.view_all_button = tk.Button(self.master, text="Ver Todos los Paquetes", command=self.view_all)
        self.view_all_button.pack(pady=5)

    def add_paquete(self):
        # Crear ventana para añadir un paquete
        self.add_window = tk.Toplevel(self.master)
        self.add_window.title("Añadir Paquete")

        tk.Label(self.add_window, text="Nombre:").pack(pady=5)
        self.nombre_entry = tk.Entry(self.add_window)
        self.nombre_entry.pack(pady=5)

        tk.Label(self.add_window, text="Descripción:").pack(pady=5)
        self.descripcion_entry = tk.Entry(self.add_window)
        self.descripcion_entry.pack(pady=5)

        tk.Label(self.add_window, text="Precio:").pack(pady=5)
        self.precio_entry = tk.Entry(self.add_window)
        self.precio_entry.pack(pady=5)

        tk.Label(self.add_window, text="Duración (días):").pack(pady=5)
        self.duracion_entry = tk.Entry(self.add_window)
        self.duracion_entry.pack(pady=5)

        tk.Button(self.add_window, text="Guardar", command=self.save_paquete).pack(pady=10)

    def save_paquete(self):
        nombre = self.nombre_entry.get()
        descripcion = self.descripcion_entry.get()
        precio = self.precio_entry.get()
        duracion = self.duracion_entry.get()

        if nombre and descripcion and precio and duracion:
            paquete = Paquete(nombre, descripcion, precio, duracion)
            self.paquetes.append(paquete)
            guardar_paquetes(self.paquetes, "data/paquetes.json")
            self.add_window.destroy()
            messagebox.showinfo("Éxito", "Paquete añadido correctamente.")
        else:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")

    def search_paquete(self):
        # Crear ventana para buscar un paquete
        self.search_window = tk.Toplevel(self.master)
        self.search_window.title("Buscar Paquete")

        tk.Label(self.search_window, text="Nombre del Paquete:").pack(pady=5)
        self.nombre_search_entry = tk.Entry(self.search_window)
        self.nombre_search_entry.pack(pady=5)

        tk.Button(self.search_window, text="Buscar", command=self.find_paquete).pack(pady=10)

    def find_paquete(self):
        nombre = self.nombre_search_entry.get()
        paquete = buscar_paquete(self.paquetes, nombre)

        if paquete:
            messagebox.showinfo("Resultado", paquete.mostrar_info())
        else:
            messagebox.showwarning("No Encontrado", "Paquete no encontrado.")

    def delete_paquete(self):
        # Crear ventana para eliminar un paquete
        self.delete_window = tk.Toplevel(self.master)
        self.delete_window.title("Eliminar Paquete")

        tk.Label(self.delete_window, text="Nombre del Paquete:").pack(pady=5)
        self.nombre_delete_entry = tk.Entry(self.delete_window)
        self.nombre_delete_entry.pack(pady=5)

        tk.Button(self.delete_window, text="Eliminar", command=self.remove_paquete).pack(pady=10)

    def remove_paquete(self):
        nombre = self.nombre_delete_entry.get()
        if eliminar_paquete(self.paquetes, nombre):
            guardar_paquetes(self.paquetes, "data/paquetes.json")
            self.delete_window.destroy()
            messagebox.showinfo("Éxito", "Paquete eliminado correctamente.")
        else:
            messagebox.showwarning("No Encontrado", "Paquete no encontrado.")

    def view_all(self):
        # Crear ventana para mostrar todos los paquetes
        self.view_window = tk.Toplevel(self.master)
        self.view_window.title("Ver Todos los Paquetes")

        for paquete in self.paquetes:
            tk.Label(self.view_window, text=paquete.mostrar_info()).pack(pady=5)
