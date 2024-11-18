from tkinter import *
from tkinter import messagebox, ttk
from tkcalendar import Calendar
from subte import Estacion
import mysql.connector
import datetime


# Conexión a la base de datos
def conectar_db():
    try:
        conn = mysql.connector.connect(
            host="181.47.29.35",
            user="2024-4INF-Grupo13",
            password="NitrogenoErbioItrio",
            database="2024-4INF-Grupo13"
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error de conexión: {err}")
        return None

conn = conectar_db()
if conn is not None:
    cursor = conn.cursor()
else:
    messagebox.showerror("Error", "No se pudo conectar a la base de datos.")
    exit()

# Crear la ventana principal
root = Tk()
root.geometry("500x600")
root.title("Seleccionar Estación y Línea de Subte")

# Diccionario con las líneas de subte y las estaciones correspondientes
subte_lines = {
    "A": [
        "acoyte", "peru", "piedras", "pasco", "plaza miserere", "loria", "lima", 
        "primera junta", "rio de janeiro", "flores", "saenz peña", "san pedrito", 
        "congreso", "castro barros", "alberti", "carabobo"
    ],
    "B": [
        "dorrego", "pasteur", "florida", "pueyrredon", "federico lacroze", "rosas", 
        "uruguay", "callao", "carlos pellegrini", "echeverria", "leandro n. alem", 
        "los incas", "malabia", "angel gallardo", "medrano", "carlos gardel", 
        "tronador"
    ],
    "C": [
        "general san martin", "lavalle", "avenida de mayo", "mariano moreno", "independencia", 
        "retiro", "constitucion", "diagonal norte", "san juan"
    ],
    "D": [
        "plaza italia", "olleros", "ministro carranza", "tribunales", "catedral", 
        "congreso de tucuman", "scalabrini ortiz", "callao.", "palermo", 
        "facultad de medicina", "juramento", "9 de julio", "bulnes", "jose hernandez", 
        "pueyrredon.", "aguero", "jujuy"
    ],
    "E": [
        "varela", "pza. de los virreyes", "retiro e", "urquiza", "san jose", "pichincha", 
        "avenida la plata", "medalla milagrosa", "boedo", "jose maria moreno", 
        "independencia.", "bolivar", "catalinas", "general belgrano", "entre rios", 
        "emilio mitre", "correo central"
    ],
    "H": [
        "venezuela", "caseros", "cordoba", "santa fe", "corrientes", "facultad derecho", 
        "hospitales", "humberto i", "inclan", "lasheras", "once", "patricios"
    ]
}

# Función que actualiza las estaciones según la línea seleccionada
def update_stations(event=None):
    selected_line = combo_line.get()
    if selected_line in subte_lines:
        stations = subte_lines[selected_line]
        combo_station['values'] = stations
        combo_station.set('')  # Limpiar la selección de estación
    else:
        combo_station['values'] = []
        combo_station.set('')

# Crear el calendario
cal = Calendar(root, selectmode='day', year=2020, month=1, day=1,  
                mindate=datetime.date(2020, 3, 1),
                maxdate=datetime.date(2020, 11, 19),
                showweeknumbers=False,  
                showothermonthdays=False,  
                disabledbackground='lightgray', 
                disabledforeground='gray')
cal.grid(row=0, column=0, columnspan=3, pady=20)

# Etiquetas y comboboxes
label_station = Label(root, text="Selecciona una estación:", font=("Arial", 10))
label_station.grid(row=2, column=0, padx=20, pady=5, sticky="w")

combo_station = ttk.Combobox(
    state="readonly"
)
combo_station.grid(row=2, column=1, padx=20, pady=5)

label_line = Label(root, text="Selecciona una línea de subte:", font=("Arial", 10))
label_line.grid(row=1, column=0, padx=20, pady=5, sticky="w")

combo_line = ttk.Combobox(
    state="readonly",
    values=["A", "B", "C", "D", "E", "H"]
)
combo_line.grid(row=1, column=1, padx=20, pady=5)

# Conectar la función de actualización de estaciones a la selección de línea
combo_line.bind("<<ComboboxSelected>>", update_stations)

# Función para mostrar la selección
def mostrar_seleccion():
    selected_station = combo_station.get()
    selected_line = combo_line.get()
    selected_date = cal.get_date()

    if selected_station and selected_line and selected_date:
        # Crear objeto Estacion
        estacion = Estacion(selected_station, selected_line)
        # Buscar la estación en la base de datos
        station_info = estacion.buscar_estacion(cursor)
        
        if station_info:
            try:
                fecha = datetime.datetime.strptime(selected_date, "%d/%m/%y").date()
                fecha_str = fecha.strftime("%Y-%m-%d")
            except ValueError as e:
                messagebox.showerror("Error", "La fecha seleccionada no es válida.")
                return

            # Realizar la consulta para obtener el promedio de pasajeros
            query = """
            SELECT Estaciones.nombre, 
                   Estaciones.linea, 
                   PasajerosPorEstacion.fecha, 
                   AVG(PasajerosPorEstacion.cantidad) AS promedio_pasajeros
            FROM Estaciones
            INNER JOIN PasajerosPorEstacion 
                ON Estaciones.nombre = PasajerosPorEstacion.estacion
            WHERE Estaciones.nombre = %s 
              AND Estaciones.linea = %s
              AND PasajerosPorEstacion.fecha = %s
            GROUP BY Estaciones.nombre, Estaciones.linea, PasajerosPorEstacion.fecha
            ORDER BY Estaciones.linea, Estaciones.nombre, PasajerosPorEstacion.fecha
            """
            try:
                cursor.execute(query, (selected_station, selected_line, fecha_str))
                result = cursor.fetchone()
                if result:
                    promedio_pasajeros = result[3]  # Obtener el promedio de pasajeros
                    messagebox.showinfo("Promedio de Pasajeros", f"El promedio de pasajeros es: {promedio_pasajeros:.2f}")
                else:
                    messagebox.showwarning("No encontrado", "No se encontraron datos para la estación y fecha seleccionada.")
            except mysql.connector.Error as err:
                messagebox.showerror("Error", "Hubo un error al consultar la base de datos.")
        else:
            messagebox.showwarning("Estación no encontrada", "La estación seleccionada no existe en la base de datos.")
    else:
        messagebox.showwarning("Campos incompletos", "Por favor, completa todos los campos.")

# Botón para mostrar la información
button_show = Button(root, text="Mostrar Promedio", command=mostrar_seleccion)
button_show.grid(row=3, column=0, columnspan=3, pady=20)



# Iniciar la interfaz gráfica
root.mainloop()
