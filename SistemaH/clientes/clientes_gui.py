import tkinter as tk
from tkinter import messagebox
from clientes.cliente import Cliente, guardar_clientes, cargar_clientes, buscar_cliente, eliminar_cliente

class GestionClientesGUI:
    """
    Clase para la gestión gráfica de clientes usando Tkinter.
    """

    def __init__(self, master):
        """
        Inicializa la interfaz de gestión de clientes.

        Parámetros:
        -----------
        master : Tk
            Ventana principal de la aplicación.
        """
        self.master = master
        self.master.title("Gestión de Clientes")
        self.master.geometry("600x400")

        # Carga inicial de clientes desde el archivo.
        self.clientes = cargar_clientes()

        self.create_widgets()

    def create_widgets(self):
        """
        Crea los widgets de la interfaz gráfica.
        """
        # Título
        self.label = tk.Label(self.master, text="Gestión de Clientes", font=("Arial", 16))
        self.label.pack(pady=10)

        # Botones de la interfaz
        self.add_cliente_button = tk.Button(self.master, text="Añadir Cliente", command=self.add_cliente)
        self.add_cliente_button.pack(pady=5)

        self.search_cliente_button = tk.Button(self.master, text="Buscar Cliente", command=self.search_cliente)
        self.search_cliente_button.pack(pady=5)

        self.delete_cliente_button = tk.Button(self.master, text="Eliminar Cliente", command=self.delete_cliente)
        self.delete_cliente_button.pack(pady=5)

        self.view_all_button = tk.Button(self.master, text="Ver Todos los Clientes", command=self.view_all)
        self.view_all_button.pack(pady=5)

    def add_cliente(self):
        """
        Abre una ventana para añadir un nuevo cliente.
        """
        self.form_window("Añadir Cliente", self.save_new_client)

    def search_cliente(self):
        """
        Abre una ventana para buscar un cliente.
        """
        self.form_window("Buscar Cliente", self.find_client)

    def delete_cliente(self):
        """
        Abre una ventana para eliminar un cliente.
        """
        self.form_window("Eliminar Cliente", self.remove_client)

    def view_all(self):
        """
        Muestra la información de todos los clientes registrados.
        """
        clientes_info = "\n".join([cliente.mostrar_info() for cliente in self.clientes])
        if not clientes_info:
            clientes_info = "No hay clientes registrados."
        messagebox.showinfo("Clientes Registrados", clientes_info)

    def form_window(self, title, action):
        """
        Crea una ventana de formulario para capturar datos del cliente.

        Parámetros:
        -----------
        title : str
            Título de la ventana de formulario.
        action : function
            Acción a ejecutar cuando se confirma el formulario.
        """
        form = tk.Toplevel(self.master)
        form.title(title)
        form.geometry("300x200")

        tk.Label(form, text="Nombre:").pack(pady=5)
        name_entry = tk.Entry(form)
        name_entry.pack(pady=5)

        tk.Label(form, text="Email:").pack(pady=5)
        email_entry = tk.Entry(form)
        email_entry.pack(pady=5)

        tk.Button(form, text="Aceptar", command=lambda: action(name_entry.get(), email_entry.get(), form)).pack(pady=10)

    def save_new_client(self, nombre, email, form):
        """
        Guarda un nuevo cliente.

        Parámetros:
        -----------
        nombre : str
            Nombre del cliente.
        email : str
            Correo electrónico del cliente.
        form : Toplevel
            Ventana de formulario a cerrar después de guardar.
        """
        if nombre and email:
            cliente = Cliente(nombre, email)
            self.clientes.append(cliente)
            guardar_clientes(self.clientes)
            messagebox.showinfo("Éxito", "Cliente añadido con éxito.")
            form.destroy()
        else:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")

    def find_client(self, nombre, email, form):
        """
        Busca un cliente y muestra su información.

        Parámetros:
        -----------
        nombre : str
            Nombre del cliente.
        email : str
            Correo electrónico del cliente.
        form : Toplevel
            Ventana de formulario a cerrar después de la búsqueda.
        """
        criterio = nombre or email
        cliente = buscar_cliente(self.clientes, criterio)
        if cliente:
            messagebox.showinfo("Cliente Encontrado", cliente.mostrar_info())
        else:
            messagebox.showwarning("No Encontrado", "Cliente no encontrado.")
        form.destroy()

    def remove_client(self, nombre, email, form):
        """
        Elimina un cliente de la lista.

        Parámetros:
        -----------
        nombre : str
            Nombre del cliente.
        email : str
            Correo electrónico del cliente.
        form : Toplevel
            Ventana de formulario a cerrar después de eliminar.
        """
        criterio = nombre or email
        if eliminar_cliente(self.clientes, criterio):
            guardar_clientes(self.clientes)
            messagebox.showinfo("Éxito", "Cliente eliminado con éxito.")
        else:
            messagebox.showwarning("No Encontrado", "Cliente no encontrado.")
        form.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = GestionClientesGUI(root)
    root.mainloop()
