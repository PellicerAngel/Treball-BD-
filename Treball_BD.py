import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sqlite3

class FitDiaryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("FitDiary - Registro e Inicio de Sesión")
        self.usuario_actual = None
        self.registros_entrenamiento = []
        self.conexion_bd = sqlite3.connect("fitdiary.db")
        self.crear_tablas()

        self.mostrar_inicio_sesion()

    def crear_tablas(self):
        cursor = self.conexion_bd.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            usuario TEXT UNIQUE,
                            contraseña TEXT,
                            edad INTEGER,
                            dni TEXT UNIQUE,
                            altura REAL,
                            genero TEXT,
                            peso REAL,
                            grasa_corporal REAL
                            )''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS registros_entrenamiento (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            usuario_id INTEGER,
                            fecha TEXT,
                            duracion INTEGER,
                            tipo_entrenamiento TEXT,
                            FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
                            )''')
        self.conexion_bd.commit()

    def mostrar_inicio_sesion(self):
        if hasattr(self, 'menu_frame'):
            self.menu_frame.destroy()
        self.frame = tk.Frame(self.root, bg="#f0f0f0")
        self.frame.pack(padx=20, pady=20)

        # Labels
        tk.Label(self.frame, text="Usuario:", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
        tk.Label(self.frame, text="Contraseña:", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=1, column=0, sticky="w", padx=5, pady=5)

        # Entries
        self.usuario_entry = tk.Entry(self.frame, bg="white", font=("Helvetica", 12))
        self.usuario_entry.grid(row=0, column=1, padx=5, pady=5)
        self.password_entry = tk.Entry(self.frame, show="*", bg="white", font=("Helvetica", 12))
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)

        # Buttons
        self.login_button = tk.Button(self.frame, text="Iniciar Sesión", command=self.iniciar_sesion, bg="#4CAF50", fg="white", font=("Helvetica", 12))
        self.login_button.grid(row=2, column=0, columnspan=2, pady=10)
        self.register_button = tk.Button(self.frame, text="Crear Usuario", command=self.mostrar_formulario_registro, bg="#1976D2", fg="white", font=("Helvetica", 12))
        self.register_button.grid(row=3, column=0, columnspan=2, pady=10)

    def mostrar_formulario_registro(self):
        self.frame.destroy()
        self.registro_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.registro_frame.pack(padx=20, pady=20)

        # Labels
        tk.Label(self.registro_frame, text="Usuario:", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
        tk.Label(self.registro_frame, text="Contraseña:", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=1, column=0, sticky="w", padx=5, pady=5)
        tk.Label(self.registro_frame, text="Edad:", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=2, column=0, sticky="w", padx=5, pady=5)
        tk.Label(self.registro_frame, text="DNI:", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=3, column=0, sticky="w", padx=5, pady=5)
        tk.Label(self.registro_frame, text="Altura (cm):", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=4, column=0, sticky="w", padx=5, pady=5)
        tk.Label(self.registro_frame, text="Género:", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=5, column=0, sticky="w", padx=5, pady=5)
        tk.Label(self.registro_frame, text="Peso (kg):", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=6, column=0, sticky="w", padx=5, pady=5)
        tk.Label(self.registro_frame, text="Grasa Corporal (%):", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=7, column=0, sticky="w", padx=5, pady=5)

        # Entries
        self.usuario_entry = tk.Entry(self.registro_frame, bg="white", font=("Helvetica", 12))
        self.usuario_entry.grid(row=0, column=1, padx=5, pady=5)
        self.password_entry = tk.Entry(self.registro_frame, show="*", bg="white", font=("Helvetica", 12))
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)
        self.edad_entry = tk.Entry(self.registro_frame, bg="white", font=("Helvetica", 12))
        self.edad_entry.grid(row=2, column=1, padx=5, pady=5)
        self.dni_entry = tk.Entry(self.registro_frame, bg="white", font=("Helvetica", 12))
        self.dni_entry.grid(row=3, column=1, padx=5, pady=5)
        self.altura_entry = tk.Entry(self.registro_frame, bg="white", font=("Helvetica", 12))
        self.altura_entry.grid(row=4, column=1, padx=5, pady=5)
        self.genero_combobox = ttk.Combobox(self.registro_frame, values=["Masculino", "Femenino"], state="readonly")
        self.genero_combobox.grid(row=5, column=1, padx=5, pady=5)
        self.peso_entry = tk.Entry(self.registro_frame, bg="white", font=("Helvetica", 12))
        self.peso_entry.grid(row=6, column=1, padx=5, pady=5)
        self.grasa_corporal_entry = tk.Entry(self.registro_frame, bg="white", font=("Helvetica", 12))
        self.grasa_corporal_entry.grid(row=7, column=1, padx=5, pady=5)

        # Buttons
        self.submit_button = tk.Button(self.registro_frame, text="Registrarse", command=self.registrar_usuario, bg="#4CAF50", fg="white", font=("Helvetica", 12))
        self.submit_button.grid(row=8, column=0, pady=10)
        self.cancel_button = tk.Button(self.registro_frame, text="Cancelar", command=self.mostrar_inicio_sesion, bg="#f44336", fg="white", font=("Helvetica", 12))
        self.cancel_button.grid(row=8, column=1, pady=10)

    def iniciar_sesion(self):
        usuario = self.usuario_entry.get()
        password = self.password_entry.get()

        cursor = self.conexion_bd.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE usuario = ? AND contraseña = ?", (usuario, password))
        usuario_encontrado = cursor.fetchone()

        if usuario_encontrado:
            self.usuario_actual = usuario
            self.mostrar_menu()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

    def mostrar_menu(self):
        if hasattr(self, 'frame'):
            self.frame.destroy()
        if hasattr(self, 'registro_frame'):
            self.registro_frame.destroy()
        self.menu_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.menu_frame.pack(padx=20, pady=20)

        # Label
        tk.Label(self.menu_frame, text=f"Bienvenido a FitDiary, {self.usuario_actual}!", bg="#f0f0f0", font=("Helvetica", 14, "bold")).grid(row=0, columnspan=2, pady=10)

        # Buttons
        self.modificar_datos_button = tk.Button(self.menu_frame, text="Modificar Datos Personales", command=self.mostrar_modificar_datos, bg="#1976D2", fg="white", font=("Helvetica", 12))
        self.modificar_datos_button.grid(row=1, columnspan=2, pady=10)
        self.registro_button = tk.Button(self.menu_frame, text="Crear Registro de Entrenamiento", command=self.crear_registro, bg="#1976D2", fg="white", font=("Helvetica", 12))
        self.registro_button.grid(row=2, columnspan=2, pady=10)
        self.ver_entrenamientos_button = tk.Button(self.menu_frame, text="Ver Entrenamientos", command=self.mostrar_progreso, bg="#1976D2", fg="white", font=("Helvetica", 12))
        self.ver_entrenamientos_button.grid(row=3, columnspan=2, pady=10)
        self.logout_button = tk.Button(self.menu_frame, text="Cerrar Sesión", command=self.cerrar_sesion, bg="#1976D2", fg="white", font=("Helvetica", 12))
        self.logout_button.grid(row=4, columnspan=2, pady=10)

    def mostrar_modificar_datos(self):
        if hasattr(self, 'menu_frame'):
            self.menu_frame.destroy()
        self.modificar_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.modificar_frame.pack(padx=20, pady=20)

        # Labels
        tk.Label(self.modificar_frame, text="Nombre:", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
        tk.Label(self.modificar_frame, text="DNI:", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=1, column=0, sticky="w", padx=5, pady=5)
        tk.Label(self.modificar_frame, text="Edad:", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=2, column=0, sticky="w", padx=5, pady=5)
        tk.Label(self.modificar_frame, text="Altura (cm):", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=3, column=0, sticky="w", padx=5, pady=5)
        tk.Label(self.modificar_frame, text="Contraseña:", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=4, column=0, sticky="w", padx=5, pady=5)
        tk.Label(self.modificar_frame, text="Peso (kg):", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=5, column=0, sticky="w", padx=5, pady=5)
        tk.Label(self.modificar_frame, text="Grasa Corporal (%):", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=6, column=0, sticky="w", padx=5, pady=5)

        # Entries
        usuario_actual_data = self.obtener_datos_usuario_actual()
        self.nombre_entry = tk.Entry(self.modificar_frame, bg="white", font=("Helvetica", 12))
        self.nombre_entry.insert(0, usuario_actual_data[0])
        self.nombre_entry.grid(row=0, column=1, padx=5, pady=5)
        self.dni_label = tk.Label(self.modificar_frame, text=usuario_actual_data[1], bg="#f0f0f0", font=("Helvetica", 12))
        self.dni_label.grid(row=1, column=1, padx=5, pady=5)
        self.edad_entry = tk.Entry(self.modificar_frame, bg="white", font=("Helvetica", 12))
        self.edad_entry.insert(0, usuario_actual_data[2])
        self.edad_entry.grid(row=2, column=1, padx=5, pady=5)
        self.altura_entry = tk.Entry(self.modificar_frame, bg="white", font=("Helvetica", 12))
        self.altura_entry.insert(0, usuario_actual_data[3])
        self.altura_entry.grid(row=3, column=1, padx=5, pady=5)
        self.contraseña_entry = tk.Entry(self.modificar_frame, bg="white", font=("Helvetica", 12))
        self.contraseña_entry.grid(row=4, column=1, padx=5, pady=5)
        self.peso_entry = tk.Entry(self.modificar_frame, bg="white", font=("Helvetica", 12))
        self.peso_entry.insert(0, usuario_actual_data[4])
        self.peso_entry.grid(row=5, column=1, padx=5, pady=5)
        self.grasa_corporal_entry = tk.Entry(self.modificar_frame, bg="white", font=("Helvetica", 12))
        self.grasa_corporal_entry.insert(0, usuario_actual_data[5])
        self.grasa_corporal_entry.grid(row=6, column=1, padx=5, pady=5)

        # Buttons
        self.guardar_button = tk.Button(self.modificar_frame, text="Guardar Cambios", command=self.guardar_cambios, bg="#4CAF50", fg="white", font=("Helvetica", 12))
        self.guardar_button.grid(row=7, columnspan=2, pady=10)
        self.cancelar_button = tk.Button(self.modificar_frame, text="Cancelar", command=self.mostrar_menu, bg="#f44336", fg="white", font=("Helvetica", 12))
        self.cancelar_button.grid(row=8, columnspan=2, pady=10)

    def obtener_datos_usuario_actual(self):
        cursor = self.conexion_bd.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE usuario = ?", (self.usuario_actual,))
        return cursor.fetchone()[1:-1]

    def guardar_cambios(self):
        nuevo_nombre = self.nombre_entry.get()
        nueva_edad = self.edad_entry.get()
        nueva_altura = self.altura_entry.get()
        nueva_contraseña = self.contraseña_entry.get()
        nuevo_peso = self.peso_entry.get()
        nueva_grasa_corporal = self.grasa_corporal_entry.get()

        cursor = self.conexion_bd.cursor()
        cursor.execute('''UPDATE usuarios SET usuario=?, edad=?, altura=?, contraseña=?, peso=?, grasa_corporal=? WHERE usuario=?''',
                        (nuevo_nombre, nueva_edad, nueva_altura, nueva_contraseña, nuevo_peso, nueva_grasa_corporal, self.usuario_actual))
        self.conexion_bd.commit()
        self.usuario_actual = nuevo_nombre
        self.mostrar_menu()

    def crear_registro(self):
        if hasattr(self, 'menu_frame'):
            self.menu_frame.destroy()
        self.registro_entrenamiento_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.registro_entrenamiento_frame.pack(padx=20, pady=20)

        # Labels
        tk.Label(self.registro_entrenamiento_frame, text="Duración (min):", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
        tk.Label(self.registro_entrenamiento_frame, text="Tipo de Entrenamiento:", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=1, column=0, sticky="w", padx=5, pady=5)

        # Entries
        self.duracion_entry = tk.Entry(self.registro_entrenamiento_frame, bg="white", font=("Helvetica", 12))
        self.duracion_entry.grid(row=0, column=1, padx=5, pady=5)
        self.tipo_entrenamiento_combobox = ttk.Combobox(self.registro_entrenamiento_frame, values=["Cardio", "Fuerza", "Flexibilidad"], state="readonly")
        self.tipo_entrenamiento_combobox.grid(row=1, column=1, padx=5, pady=5)

        # Buttons
        self.guardar_registro_button = tk.Button(self.registro_entrenamiento_frame, text="Guardar Registro", command=self.guardar_registro, bg="#4CAF50", fg="white", font=("Helvetica", 12))
        self.guardar_registro_button.grid(row=2, columnspan=2, pady=10)
        self.cancelar_registro_button = tk.Button(self.registro_entrenamiento_frame, text="Cancelar", command=self.mostrar_menu, bg="#f44336", fg="white", font=("Helvetica", 12))
        self.cancelar_registro_button.grid(row=3, columnspan=2, pady=10)

    def guardar_registro(self):
        duracion = self.duracion_entry.get()
        tipo_entrenamiento = self.tipo_entrenamiento_combobox.get()
        fecha = "2024-05-03"  # Obtener la fecha actual o permitir al usuario elegir la fecha

        cursor = self.conexion_bd.cursor()
        cursor.execute('''INSERT INTO registros_entrenamiento (usuario_id, fecha, duracion, tipo_entrenamiento) VALUES (?, ?, ?, ?)''',
                       (self.obtener_id_usuario_actual(), fecha, duracion, tipo_entrenamiento))
        self.conexion_bd.commit()
        messagebox.showinfo("Registro Exitoso", "Se ha registrado el entrenamiento correctamente.")
        self.mostrar_menu()

    def obtener_id_usuario_actual(self):
        cursor = self.conexion_bd.cursor()
        cursor.execute("SELECT id FROM usuarios WHERE usuario = ?", (self.usuario_actual,))
        return cursor.fetchone()[0]

    def mostrar_progreso(self):
        if hasattr(self, 'menu_frame'):
            self.menu_frame.destroy()
        self.progreso_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.progreso_frame.pack(padx=20, pady=20)

        # Obtener registros de entrenamiento del usuario actual
        cursor = self.conexion_bd.cursor()
        cursor.execute("SELECT COUNT(id), fecha, duracion, tipo_entrenamiento FROM registros_entrenamiento WHERE usuario_id = ? GROUP BY fecha, duracion, tipo_entrenamiento",
                       (self.obtener_id_usuario_actual(),))
        registros = cursor.fetchall()

        # Treeview
        tree = ttk.Treeview(self.progreso_frame, columns=("Fecha", "Duración (min)", "Tipo de Entrenamiento", "Total Registros"))
        tree.heading("#0", text="ID")
        tree.heading("Fecha", text="Fecha")
        tree.heading("Duración (min)", text="Duración (min)")
        tree.heading("Tipo de Entrenamiento", text="Tipo de Entrenamiento")
        tree.heading("Total Registros", text="Total Registros")
        
        for i, registro in enumerate(registros, start=1):
            tree.insert("", "end", text=i, values=(registro[1], registro[2], registro[3], registro[0]))
        
        tree.pack(pady=10)

        # Button
        self.volver_button = tk.Button(self.progreso_frame, text="Volver", command=self.mostrar_menu, bg="#1976D2", fg="white", font=("Helvetica", 12))
        self.volver_button.pack(pady=10)

    def cerrar_sesion(self):
        self.usuario_actual = None
        self.mostrar_inicio_sesion()

    def registrar_usuario(self):
        usuario = self.usuario_entry.get()
        contraseña = self.password_entry.get()
        edad = self.edad_entry.get()
        dni = self.dni_entry.get()
        altura = self.altura_entry.get()
        genero = self.genero_combobox.get()
        peso = self.peso_entry.get()
        grasa_corporal = self.grasa_corporal_entry.get()

        if not usuario or not contraseña or not edad or not dni or not altura or not genero or not peso or not grasa_corporal:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
            return

        cursor = self.conexion_bd.cursor()
        try:
            cursor.execute('''INSERT INTO usuarios (usuario, contraseña, edad, dni, altura, genero, peso, grasa_corporal)
                              VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', (usuario, contraseña, edad, dni, altura, genero, peso, grasa_corporal))
            self.conexion_bd.commit()
            messagebox.showinfo("Registro Exitoso", "Usuario registrado exitosamente.")
            self.mostrar_inicio_sesion()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "El usuario o el DNI ya están en uso.")

root = tk.Tk()
app = FitDiaryApp(root)
root.mainloop()
