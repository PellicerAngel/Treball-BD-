import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sqlite3
from datetime import datetime

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
        self.guardar_button = tk.Button(self.registro_frame, text="Guardar", command=self.registrar_usuario, bg="#4CAF50", fg="white", font=("Helvetica", 12))
        self.guardar_button.grid(row=8, column=0, pady=10)
        self.cancel_button = tk.Button(self.registro_frame, text="Cancelar", command=self.mostrar_inicio_sesion, bg="#f44336", fg="white", font=("Helvetica", 12))
        self.cancel_button.grid(row=8, column=1, pady=10)

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
        self.guardar_button = tk.Button(self.registro_frame, text="Guardar", command=self.registrar_usuario, bg="#4CAF50", fg="white", font=("Helvetica", 12))
        self.guardar_button.grid(row=8, column=0, pady=10)
        self.cancel_button = tk.Button(self.registro_frame, text="Cancelar", command=self.mostrar_inicio_sesion, bg="#f44336", fg="white", font=("Helvetica", 12))
        self.cancel_button.grid(row=8, column=1, pady=10)

    def mostrar_formulario_registro_entrenamiento(self):
        self.frame.destroy()
        self.registro_entrenamiento_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.registro_entrenamiento_frame.pack(padx=20, pady=20)

        # Labels
        tk.Label(self.registro_entrenamiento_frame, text="Duración (min):", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
        tk.Label(self.registro_entrenamiento_frame, text="Tipo de Entrenamiento:", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=1, column=0, sticky="w", padx=5, pady=5)

        # Entries
        self.duracion_entry = tk.Entry(self.registro_entrenamiento_frame, bg="white", font=("Helvetica", 12))
        self.duracion_entry.grid(row=0, column=1, padx=5, pady=5)
        self.tipo_entrenamiento_entry = tk.Entry(self.registro_entrenamiento_frame, bg="white", font=("Helvetica", 12))
        self.tipo_entrenamiento_entry.grid(row=1, column=1, padx=5, pady=5)

        # Buttons
        self.guardar_button = tk.Button(self.registro_entrenamiento_frame, text="Guardar", command=self.registrar_entrenamiento, bg="#4CAF50", fg="white", font=("Helvetica", 12))
        self.guardar_button.grid(row=2, column=0, pady=10)
        self.cancel_button = tk.Button(self.registro_entrenamiento_frame, text="Cancelar", command=self.mostrar_menu_principal, bg="#f44336", fg="white", font=("Helvetica", 12))
        self.cancel_button.grid(row=2, column=1, pady=10)

    def registrar_entrenamiento(self):
        duracion = self.duracion_entry.get()
        tipo_entrenamiento = self.tipo_entrenamiento_entry.get()

        if not duracion or not tipo_entrenamiento:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
            return

        cursor = self.conexion_bd.cursor()
        cursor.execute('''INSERT INTO registros_entrenamiento (usuario_id, fecha, duracion, tipo_entrenamiento)
                          VALUES (?, ?, ?, ?)''', (self.usuario_actual[0], datetime.now(), duracion, tipo_entrenamiento))
        self.conexion_bd.commit()
        messagebox.showinfo("Registro de Entrenamiento", "Registro de entrenamiento exitoso.")
        self.mostrar_menu_principal()

    def iniciar_sesion(self):
        usuario = self.usuario_entry.get()
        contraseña = self.password_entry.get()

        cursor = self.conexion_bd.cursor()
        cursor.execute('''SELECT * FROM usuarios WHERE usuario = ? AND contraseña = ?''', (usuario, contraseña))
        usuario = cursor.fetchone()

        if usuario:
            self.usuario_actual = usuario
            self.mostrar_menu_principal()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

    def mostrar_menu_principal(self):
        if hasattr(self, 'frame'):
            self.frame.destroy()
        if hasattr(self, 'registro_frame'):
            self.registro_frame.destroy()
        if hasattr(self, 'registro_entrenamiento_frame'):
            self.registro_entrenamiento_frame.destroy()

        self.menu_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.menu_frame.pack(padx=20, pady=20)

        tk.Label(self.menu_frame, text=f"Bienvenido, {self.usuario_actual[1]}!", bg="#f0f0f0", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=10)
        tk.Button(self.menu_frame, text="Registrar Entrenamiento", command=self.mostrar_formulario_registro_entrenamiento, bg="#1976D2", fg="white", font=("Helvetica", 12)).grid(row=1, column=0, padx=10, pady=10)
        tk.Button(self.menu_frame, text="Cerrar Sesión", command=self.mostrar_inicio_sesion, bg="#f44336", fg="white", font=("Helvetica", 12)).grid(row=1, column=1, padx=10, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = FitDiaryApp(root)
    root.mainloop()
