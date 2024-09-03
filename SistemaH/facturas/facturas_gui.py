import tkinter as tk
from tkinter import messagebox
from .gestion_facturas import (guardar_facturas, cargar_facturas, buscar_factura, eliminar_factura)
from .factura import Factura
from datetime import datetime

class GestionFacturasGUI:
    """
    Clase que representa la interfaz gráfica para la gestión de facturas.

    Métodos:
        create_widgets(): Crea los widgets de la interfaz gráfica.
        add_factura(): Muestra una ventana para añadir una nueva factura.
        save_factura(): Guarda una nueva factura.
        search_factura(): Muestra una ventana para buscar una factura.
        find_factura(): Busca y muestra una factura.
        update_factura(): Muestra una ventana para actualizar una factura.
        load_factura_for_update(): Carga una factura para actualización.
        save_updated_factura(factura): Guarda la factura actualizada.
        delete_factura(): Muestra una ventana para eliminar una factura.
        remove_factura(): Elimina una factura.
        view_all(): Muestra todas las facturas.
    """
    def __init__(self, master):
        self.master = master
        self.master.title("Gestión de Facturación")

        self.facturas = cargar_facturas("data/facturas.json")

        self.create_widgets()

    def create_widgets(self):
        """
        Crea los widgets de la interfaz gráfica.
        """
        self.label = tk.Label(self.master, text="Gestión de Facturación", font=("Arial", 14))
        self.label.pack(pady=10)

        self.add_factura_button = tk.Button(self.master, text="Añadir Factura", command=self.add_factura)
        self.add_factura_button.pack(pady=5)

        self.search_factura_button = tk.Button(self.master, text="Buscar Factura", command=self.search_factura)
        self.search_factura_button.pack(pady=5)

        self.update_factura_button = tk.Button(self.master, text="Actualizar Factura", command=self.update_factura)
        self.update_factura_button.pack(pady=5)

        self.delete_factura_button = tk.Button(self.master, text="Eliminar Factura", command=self.delete_factura)
        self.delete_factura_button.pack(pady=5)

        self.view_all_button = tk.Button(self.master, text="Ver Todas las Facturas", command=self.view_all)
        self.view_all_button.pack(pady=5)

    def add_factura(self):
        """
        Muestra una ventana para añadir una nueva factura.
        """
        self.add_window = tk.Toplevel(self.master)
        self.add_window.title("Añadir Factura")

        tk.Label(self.add_window, text="Número de Factura:").pack(pady=5)
        self.numero_entry = tk.Entry(self.add_window)
        self.numero_entry.pack(pady=5)

        tk.Label(self.add_window, text="Nombre del Cliente:").pack(pady=5)
        self.cliente_entry = tk.Entry(self.add_window)
        self.cliente_entry.pack(pady=5)

        tk.Label(self.add_window, text="Descripción:").pack(pady=5)
        self.descripcion_entry = tk.Entry(self.add_window)
        self.descripcion_entry.pack(pady=5)

        tk.Label(self.add_window, text="Monto Total:").pack(pady=5)
        self.monto_entry = tk.Entry(self.add_window)
        self.monto_entry.pack(pady=5)

        tk.Label(self.add_window, text="Fecha de Emisión (YYYY-MM-DD):").pack(pady=5)
        self.fecha_entry = tk.Entry(self.add_window)
        self.fecha_entry.pack(pady=5)

        tk.Button(self.add_window, text="Guardar", command=self.save_factura).pack(pady=10)

    def save_factura(self):
        """
        Guarda una nueva factura.
        """
        numero = self.numero_entry.get()
        cliente = self.cliente_entry.get()
        descripcion = self.descripcion_entry.get()
        monto = self.monto_entry.get()
        fecha = self.fecha_entry.get()

        try:
            fecha = datetime.strptime(fecha, "%Y-%m-%d").date()
        except ValueError:
            messagebox.showwarning("Advertencia", "Fecha inválida. Use el formato YYYY-MM-DD.")
            return

        factura = Factura(numero, cliente, descripcion, monto, fecha)
        self.facturas.append(factura)
        guardar_facturas(self.facturas, "data/facturas.json")
        self.add_window.destroy()
        messagebox.showinfo("Éxito", "Factura añadida correctamente.")

    def search_factura(self):
        """
        Muestra una ventana para buscar una factura.
        """
        self.search_window = tk.Toplevel(self.master)
        self.search_window.title("Buscar Factura")

        tk.Label(self.search_window, text="Número de Factura:").pack(pady=5)
        self.numero_search_entry = tk.Entry(self.search_window)
        self.numero_search_entry.pack(pady=5)

        tk.Button(self.search_window, text="Buscar", command=self.find_factura).pack(pady=10)

    def find_factura(self):
        """
        Busca y muestra una factura.
        """
        numero = self.numero_search_entry.get()
        factura = buscar_factura(self.facturas, numero)

        if factura:
            messagebox.showinfo("Resultado", factura.mostrar_info())
        else:
            messagebox.showwarning("No Encontrado", "Factura no encontrada.")

    def update_factura(self):
        """
        Muestra una ventana para actualizar una factura.
        """
        self.update_window = tk.Toplevel(self.master)
        self.update_window.title("Actualizar Factura")

        tk.Label(self.update_window, text="Número de Factura:").pack(pady=5)
        self.numero_update_entry = tk.Entry(self.update_window)
        self.numero_update_entry.pack(pady=5)

        tk.Button(self.update_window, text="Cargar", command=self.load_factura_for_update).pack(pady=10)

    def load_factura_for_update(self):
        """
        Carga una factura para actualización.
        """
        numero = self.numero_update_entry.get()
        self.factura = buscar_factura(self.facturas, numero)

        if self.factura:
            self.update_window.destroy()
            self.add_factura()
            self.numero_entry.insert(0, self.factura.numero_factura)
            self.cliente_entry.insert(0, self.factura.cliente)
            self.descripcion_entry.insert(0, self.factura.descripcion)
            self.monto_entry.insert(0, self.factura.monto_total)
            self.fecha_entry.insert(0, str(self.factura.fecha_emision))
            tk.Button(self.add_window, text="Actualizar", command=lambda: self.save_updated_factura(self.factura)).pack(pady=10)
        else:
            messagebox.showwarning("No Encontrado", "Factura no encontrada.")

    def save_updated_factura(self, factura):
        """
        Guarda la factura actualizada.
        """
        factura.actualizar_info(
            cliente=self.cliente_entry.get(),
            descripcion=self.descripcion_entry.get(),
            monto_total=self.monto_entry.get(),
            fecha_emision=datetime.strptime(self.fecha_entry.get(), "%Y-%m-%d").date()
        )
        guardar_facturas(self.facturas, "data/facturas.json")
        self.add_window.destroy()
        messagebox.showinfo("Éxito", "Factura actualizada correctamente.")

    def delete_factura(self):
        """
        Muestra una ventana para eliminar una factura.
        """
        self.delete_window = tk.Toplevel(self.master)
        self.delete_window.title("Eliminar Factura")

        tk.Label(self.delete_window, text="Número de Factura:").pack(pady=5)
        self.numero_delete_entry = tk.Entry(self.delete_window)
        self.numero_delete_entry.pack(pady=5)

        tk.Button(self.delete_window, text="Eliminar", command=self.remove_factura).pack(pady=10)

    def remove_factura(self):
        """
        Elimina una factura.
        """
        numero = self.numero_delete_entry.get()
        if eliminar_factura(self.facturas, numero):
            guardar_facturas(self.facturas, "data/facturas.json")
            messagebox.showinfo("Éxito", "Factura eliminada correctamente.")
        else:
            messagebox.showwarning("No Encontrado", "Factura no encontrada.")
        self.delete_window.destroy()

    def view_all(self):
        """
        Muestra todas las facturas.
        """
        facturas_info = "\n\n".join([factura.mostrar_info() for factura in self.facturas])
        if facturas_info:
            messagebox.showinfo("Todas las Facturas", facturas_info)
        else:
            messagebox.showinfo("Sin Facturas", "No hay facturas disponibles.")
