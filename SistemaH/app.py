import tkinter as tk
from tkinter import ttk
from clientes.clientes_gui import GestionClientesGUI
from paquetes.paquetes_gui import GestionPaquetesGUI
from hoteles.hoteles_gui import main as gestionar_hoteles
from vuelos.vuelos_gui import GestionVuelosGUI
from facturas.facturas_gui import GestionFacturasGUI  # Corrige el nombre de la clase

class App:
    def __init__(self, root):
        """
        Inicializa la aplicación con la ventana principal y los widgets.
        
        Args:
        root (tk.Tk): La ventana principal de Tkinter.
        """
        self.root = root
        self.root.title("Aplicación de Gestión de Agencia de Viajes")
        self.create_widgets()

    def create_widgets(self):
        """
        Crea y organiza los widgets en la ventana principal.
        """
        # Etiqueta principal
        self.label = tk.Label(self.root, text="Bienvenido a la aplicación de gestión de viajes", font=("Arial", 16))
        self.label.pack(pady=20)

        # Crear un marco para los botones
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=20)

        # Botones para cada sección de la aplicación
        self.clientes_button = tk.Button(button_frame, text="Clientes", command=self.gestionar_clientes)
        self.clientes_button.grid(row=0, column=0, padx=10, pady=5)

        self.paquetes_button = tk.Button(button_frame, text="Paquetes Turísticos", command=self.gestionar_paquetes)
        self.paquetes_button.grid(row=0, column=1, padx=10, pady=5)

        self.vuelos_button = tk.Button(button_frame, text="Reservas de Vuelos", command=self.gestionar_vuelos)
        self.vuelos_button.grid(row=1, column=0, padx=10, pady=5)

        self.hoteles_button = tk.Button(button_frame, text="Reservas de Hoteles", command=self.gestionar_hoteles)
        self.hoteles_button.grid(row=1, column=1, padx=10, pady=5)

        self.facturacion_button = tk.Button(button_frame, text="Facturación", command=self.gestionar_facturas)
        self.facturacion_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

    def gestionar_clientes(self):
        """
        Abre una nueva ventana para la gestión de clientes.
        """
        self.open_window("Gestión de Clientes", self.gestionar_clientes_gui)

    def gestionar_paquetes(self):
        """
        Abre una nueva ventana para la gestión de paquetes turísticos.
        """
        self.open_window("Gestión de Paquetes Turísticos", self.gestionar_paquetes_gui)

    def gestionar_vuelos(self):
        """
        Abre una nueva ventana para la gestión de reservas de vuelos.
        """
        self.open_window("Gestión de Reservas de Vuelos", self.gestionar_vuelos_gui)

    def gestionar_hoteles(self):
        """
        Abre una nueva ventana para la gestión de reservas de hoteles.
        """
        self.open_window("Gestión de Reservas de Hoteles", gestionar_hoteles)

    def gestionar_facturas(self):
        """
        Abre una nueva ventana para la gestión de facturación.
        """
        self.open_window("Gestión de Facturación", self.gestionar_facturas_gui)

    def open_window(self, title, func):
        """
        Abre una nueva ventana con el título especificado y llama a la función proporcionada.
        
        Args:
        title (str): Título de la nueva ventana.
        func (callable): Función que se llamará para configurar la nueva ventana.
        """
        new_window = tk.Toplevel(self.root)
        new_window.title(title)
        new_window.geometry("600x400")
        func(new_window)

    def gestionar_clientes_gui(self, master):
        """
        Configura la interfaz gráfica para la gestión de clientes.
        
        Args:
        master (tk.Toplevel): La ventana para configurar la interfaz gráfica de clientes.
        """
        GestionClientesGUI(master)

    def gestionar_paquetes_gui(self, master):
        """
        Configura la interfaz gráfica para la gestión de paquetes turísticos.
        
        Args:
        master (tk.Toplevel): La ventana para configurar la interfaz gráfica de paquetes turísticos.
        """
        GestionPaquetesGUI(master)

    def gestionar_vuelos_gui(self, master):
        """
        Configura la interfaz gráfica para la gestión de reservas de vuelos.
        
        Args:
        master (tk.Toplevel): La ventana para configurar la interfaz gráfica de reservas de vuelos.
        """
        GestionVuelosGUI(master)

    def gestionar_facturas_gui(self, master):
        """
        Configura la interfaz gráfica para la gestión de facturación.
        
        Args:
        master (tk.Toplevel): La ventana para configurar la interfaz gráfica de facturación.
        """
        GestionFacturasGUI(master)  # Usa el nombre correcto de la clase

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
