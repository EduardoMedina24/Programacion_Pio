import tkinter as tk
from tkinter import messagebox
from vuelos.reserva_vuelo import ReservaVuelo
from vuelos.gestion_reservas_vuelo import guardar_reservas, cargar_reservas, buscar_reserva, eliminar_reserva
from datetime import datetime

class GestionVuelosGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Gestión de Reservas de Vuelos")

        self.reservas = cargar_reservas("data/reservas_vuelo.json")

        self.create_widgets()

    def create_widgets(self):
        # Crear Widgets
        self.label = tk.Label(self.master, text="Gestión de Reservas de Vuelos", font=("Arial", 14))
        self.label.pack(pady=10)

        self.add_reserva_button = tk.Button(self.master, text="Añadir Reserva", command=self.add_reserva)
        self.add_reserva_button.pack(pady=5)

        self.search_reserva_button = tk.Button(self.master, text="Buscar Reserva", command=self.search_reserva)
        self.search_reserva_button.pack(pady=5)

        self.update_reserva_button = tk.Button(self.master, text="Actualizar Reserva", command=self.update_reserva)
        self.update_reserva_button.pack(pady=5)

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

        tk.Label(self.add_window, text="Nombre del Cliente:").pack(pady=5)
        self.cliente_entry = tk.Entry(self.add_window)
        self.cliente_entry.pack(pady=5)

        tk.Label(self.add_window, text="Número de Vuelo:").pack(pady=5)
        self.vuelo_entry = tk.Entry(self.add_window)
        self.vuelo_entry.pack(pady=5)

        tk.Label(self.add_window, text="Fecha de Reserva:").pack(pady=5)
        self.fecha_reserva_entry = tk.Entry(self.add_window)
        self.fecha_reserva_entry.pack(pady=5)

        tk.Label(self.add_window, text="Fecha de Salida:").pack(pady=5)
        self.fecha_salida_entry = tk.Entry(self.add_window)
        self.fecha_salida_entry.pack(pady=5)

        tk.Label(self.add_window, text="Fecha de Llegada:").pack(pady=5)
        self.fecha_llegada_entry = tk.Entry(self.add_window)
        self.fecha_llegada_entry.pack(pady=5)

        tk.Button(self.add_window, text="Guardar", command=self.save_reserva).pack(pady=10)

    def parse_fecha(self, fecha_str):
        formatos = ["%d/%m/%Y", "%d-%m-%Y", "%d.%m.%Y", "%Y-%m-%d"]
        print(f"Intentando analizar la fecha: {fecha_str}")  # Mensaje de depuración
        for formato in formatos:
            try:
                return datetime.strptime(fecha_str, formato).date()
            except ValueError:
                print(f"Formato no válido: {formato}")  # Mensaje de depuración
                continue
        raise ValueError(f"Formato de fecha no válido: {fecha_str}")

    def save_reserva(self):
        codigo_reserva = self.codigo_reserva_entry.get()
        cliente = self.cliente_entry.get()
        vuelo = self.vuelo_entry.get()
        fecha_reserva = self.fecha_reserva_entry.get()
        fecha_salida = self.fecha_salida_entry.get()
        fecha_llegada = self.fecha_llegada_entry.get()

        try:
            fecha_reserva = self.parse_fecha(fecha_reserva)
            fecha_salida = self.parse_fecha(fecha_salida)
            fecha_llegada = self.parse_fecha(fecha_llegada)
        except ValueError as e:
            messagebox.showwarning("Advertencia", f"Fecha inválida. {e}")
            return

        reserva = ReservaVuelo(codigo_reserva, cliente, vuelo, fecha_reserva, fecha_salida, fecha_llegada)
        self.reservas.append(reserva)
        guardar_reservas(self.reservas, "data/reservas_vuelo.json")
        self.add_window.destroy()
        messagebox.showinfo("Éxito", "Reserva de vuelo añadida correctamente.")

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
        reserva = buscar_reserva(self.reservas, codigo_reserva)

        if reserva:
            messagebox.showinfo("Resultado", reserva.mostrar_info())
        else:
            messagebox.showwarning("No Encontrado", "Reserva no encontrada.")

    def update_reserva(self):
        # Crear ventana para actualizar una reserva
        self.update_window = tk.Toplevel(self.master)
        self.update_window.title("Actualizar Reserva")

        tk.Label(self.update_window, text="Código de Reserva:").pack(pady=5)
        self.codigo_reserva_update_entry = tk.Entry(self.update_window)
        self.codigo_reserva_update_entry.pack(pady=5)

        tk.Label(self.update_window, text="Nuevo Nombre del Cliente (dejar en blanco para mantener el actual):").pack(pady=5)
        self.nuevo_cliente_entry = tk.Entry(self.update_window)
        self.nuevo_cliente_entry.pack(pady=5)

        tk.Label(self.update_window, text="Nuevo Número de Vuelo (dejar en blanco para mantener el actual):").pack(pady=5)
        self.nuevo_vuelo_entry = tk.Entry(self.update_window)
        self.nuevo_vuelo_entry.pack(pady=5)

        tk.Label(self.update_window, text="Nueva Fecha de Reserva (dejar en blanco para mantener la actual):").pack(pady=5)
        self.nueva_fecha_reserva_entry = tk.Entry(self.update_window)
        self.nueva_fecha_reserva_entry.pack(pady=5)

        tk.Label(self.update_window, text="Nueva Fecha de Salida (dejar en blanco para mantener la actual):").pack(pady=5)
        self.nueva_fecha_salida_entry = tk.Entry(self.update_window)
        self.nueva_fecha_salida_entry.pack(pady=5)

        tk.Label(self.update_window, text="Nueva Fecha de Llegada (dejar en blanco para mantener la actual):").pack(pady=5)
        self.nueva_fecha_llegada_entry = tk.Entry(self.update_window)
        self.nueva_fecha_llegada_entry.pack(pady=5)

        tk.Button(self.update_window, text="Actualizar", command=self.apply_update).pack(pady=10)

    def apply_update(self):
        codigo_reserva = self.codigo_reserva_update_entry.get()
        reserva = buscar_reserva(self.reservas, codigo_reserva)

        if reserva:
            nuevo_cliente = self.nuevo_cliente_entry.get()
            nuevo_vuelo = self.nuevo_vuelo_entry.get()
            nueva_fecha_reserva = self.nueva_fecha_reserva_entry.get()
            nueva_fecha_salida = self.nueva_fecha_salida_entry.get()
            nueva_fecha_llegada = self.nueva_fecha_llegada_entry.get()

            try:
                nueva_fecha_reserva = self.parse_fecha(nueva_fecha_reserva) if nueva_fecha_reserva else None
                nueva_fecha_salida = self.parse_fecha(nueva_fecha_salida) if nueva_fecha_salida else None
                nueva_fecha_llegada = self.parse_fecha(nueva_fecha_llegada) if nueva_fecha_llegada else None
            except ValueError as e:
                messagebox.showwarning("Advertencia", f"Fecha inválida. {e}")
                return

            reserva.actualizar_info(
                cliente=nuevo_cliente if nuevo_cliente else None,
                vuelo=nuevo_vuelo if nuevo_vuelo else None,
                fecha_reserva=nueva_fecha_reserva if nueva_fecha_reserva else None,
                fecha_salida=nueva_fecha_salida if nueva_fecha_salida else None,
                fecha_llegada=nueva_fecha_llegada if nueva_fecha_llegada else None
            )
            guardar_reservas(self.reservas, "data/reservas_vuelo.json")
            self.update_window.destroy()
            messagebox.showinfo("Éxito", "Reserva de vuelo actualizada correctamente.")
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
        resultado = eliminar_reserva(self.reservas, codigo_reserva)

        if resultado:
            guardar_reservas(self.reservas, "data/reservas_vuelo.json")
            self.delete_window.destroy()
            messagebox.showinfo("Éxito", "Reserva de vuelo eliminada correctamente.")
        else:
            messagebox.showwarning("No Encontrado", "Reserva no encontrada.")

    def view_all(self):
        # Crear ventana para ver todas las reservas
        self.view_window = tk.Toplevel(self.master)
        self.view_window.title("Todas las Reservas de Vuelos")

        text_area = tk.Text(self.view_window, wrap=tk.WORD)
        text_area.pack(expand=True, fill=tk.BOTH)

        for reserva in self.reservas:
            text_area.insert(tk.END, f"{reserva.mostrar_info()}\n\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = GestionVuelosGUI(root)
    root.mainloop()
