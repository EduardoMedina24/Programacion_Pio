import tkinter as tk
from tkinter import messagebox
from .gestion_facturas import (guardar_facturas, cargar_facturas, buscar_factura, eliminar_factura)
from .factura import Factura
from datetime import datetime

class GestionFacturasGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Gestión de Facturación")

        self.facturas = cargar_facturas("data/facturas.json")

        self.create_widgets()

    def create_widgets(self):
        
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
    
        self.search_window = tk.Toplevel(self.master)
        self.search_window.title("Buscar Factura")

        tk.Label(self.search_window, text="Número de Factura:").pack(pady=5)
        self.numero_search_entry = tk.Entry(self.search_window)
        self.numero_search_entry.pack(pady=5)

        tk.Button(self.search_window, text="Buscar", command=self.find_factura).pack(pady=10)

    def find_factura(self):
        numero = self.numero_search_entry.get()
        factura = buscar_factura(self.facturas, numero)

        if factura:
            messagebox.showinfo("Resultado", factura.mostrar_info())
        else:
            messagebox.showwarning("No Encontrado", "Factura no encontrada.")

    def update_factura(self):

        self.update_window = tk.Toplevel(self.master)
        self.update_window.title("Actualizar Factura")

        tk.Label(self.update_window, text="Número de Factura:").pack(pady=5)
        self.numero_update_entry = tk.Entry(self.update_window)
        self.numero_update_entry.pack(pady=5)

        tk.Button(self.update_window, text="Buscar", command=self.load_factura_for_update).pack(pady=10)

    def load_factura_for_update(self):
        numero = self.numero_update_entry.get()
        factura = buscar_factura(self.facturas, numero)

        if factura:
            
            self.update_window.destroy()
            self.update_factura_window = tk.Toplevel(self.master)
            self.update_factura_window.title("Actualizar Factura")

            tk.Label(self.update_factura_window, text="Nombre del Cliente:").pack(pady=5)
            self.update_cliente_entry = tk.Entry(self.update_factura_window)
            self.update_cliente_entry.insert(0, factura.cliente)
            self.update_cliente_entry.pack(pady=5)

            tk.Label(self.update_factura_window, text="Descripción:").pack(pady=5)
            self.update_descripcion_entry = tk.Entry(self.update_factura_window)
            self.update_descripcion_entry.insert(0, factura.descripcion)
            self.update_descripcion_entry.pack(pady=5)

            tk.Label(self.update_factura_window, text="Monto Total:").pack(pady=5)
            self.update_monto_entry = tk.Entry(self.update_factura_window)
            self.update_monto_entry.insert(0, factura.monto_total)
            self.update_monto_entry.pack(pady=5)

            tk.Label(self.update_factura_window, text="Fecha de Emisión (YYYY-MM-DD):").pack(pady=5)
            self.update_fecha_entry = tk.Entry(self.update_factura_window)
            self.update_fecha_entry.insert(0, factura.fecha_emision)
            self.update_fecha_entry.pack(pady=5)

            tk.Button(self.update_factura_window, text="Actualizar", command=lambda: self.save_updated_factura(factura)).pack(pady=10)
        else:
            messagebox.showwarning("No Encontrado", "Factura no encontrada.")

    def save_updated_factura(self, factura):
        cliente = self.update_cliente_entry.get()
        descripcion = self.update_descripcion_entry.get()
        monto = self.update_monto_entry.get()
        fecha = self.update_fecha_entry.get()

        
        try:
            fecha = datetime.strptime(fecha, "%Y-%m-%d").date()
        except ValueError:
            messagebox.showwarning("Advertencia", "Fecha inválida. Use el formato YYYY-MM-DD.")
            return

        factura.actualizar_info(cliente=cliente, descripcion=descripcion, monto_total=monto, fecha_emision=fecha)
        guardar_facturas(self.facturas, "data/facturas.json")
        self.update_factura_window.destroy()
        messagebox.showinfo("Éxito", "Factura actualizada correctamente.")

    def delete_factura(self):
        
        self.delete_window = tk.Toplevel(self.master)
        self.delete_window.title("Eliminar Factura")

        tk.Label(self.delete_window, text="Número de Factura:").pack(pady=5)
        self.numero_delete_entry = tk.Entry(self.delete_window)
        self.numero_delete_entry.pack(pady=5)

        tk.Button(self.delete_window, text="Eliminar", command=self.remove_factura).pack(pady=10)

    def remove_factura(self):
        numero = self.numero_delete_entry.get()
        if eliminar_factura(self.facturas, numero):
            guardar_facturas(self.facturas, "data/facturas.json")
            self.delete_window.destroy()
            messagebox.showinfo("Éxito", "Factura eliminada correctamente.")
        else:
            messagebox.showwarning("No Encontrado", "Factura no encontrada.")

    def view_all(self):
        
        self.view_window = tk.Toplevel(self.master)
        self.view_window.title("Ver Todas las Facturas")

        for factura in self.facturas:
            tk.Label(self.view_window, text=factura.mostrar_info()).pack(pady=5)

def main(master):
    app = GestionFacturasGUI(master)

if __name__ == "__main__":
    pass
