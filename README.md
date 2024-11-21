## Sistema de Gestión de Estaciones de Subte ##

Este proyecto implementa una interfaz gráfica para la consulta, modificación y eliminación de registros relacionados con estaciones y líneas de subte, utilizando Python, Tkinter y MySQL.

## Descripción

La aplicación permite seleccionar una línea y una estación de subte, junto con una fecha específica, para realizar distintas acciones en la base de datos, como:
- Mostrar la suma de pasajeros en una estación y línea determinada.
- Modificar los registros asociados.
- Eliminar registros específicos.

Además, la aplicación utiliza un calendario interactivo para seleccionar la fecha y ofrece menús desplegables para facilitar la selección de líneas y estaciones.

## Instalación

1. **Clona este repositorio** [consola bash]:
   
   git clone https://github.com/usuario/sistema-subte.git
   cd sistema-subte

2. **Instala las dependencias requeridas**:
   Asegúrate de tener Python 3.8+ y pip instalados, luego ejecuta [consola bash]:
   
   pip install -r requirements.txt

3. **Configura la conexión a la base de datos**:
   Modifica segun el lugar de acceso los datos de conexión en la función `conectar_db() [editor de python]:

   |Estando en el Pio|
   conn = mysql.connector.connect(
       host="10.1.5.205", 
       user="2024-4INF-Grupo13",
       password="NitrogenoErbioItrio",
       database="2024-4INF-Grupo13"
   )
   |Estando fuera del pio|
   conn = mysql.connector.connect(
       host="181.47.29.35", 
       user="4INF",
       password="NitrogenoErbioItrio",
       database="2024-4INF-Grupo13"
   )

   Asegúrate de que los datos sean correctos y que tengas acceso a la base de datos.

5. **Ejecuta la aplicación**:

## Uso

1. **Selecciona una línea de subte**:
   Utiliza el menú desplegable para elegir la línea (por ejemplo, A, B, C, etc.).

2. **Selecciona una estación**:
   Una vez seleccionada la línea, se actualizarán automáticamente las estaciones disponibles.

3. **Elige una fecha**:
   Usa el calendario interactivo para seleccionar una fecha válida.

4. **Selecciona una función**:
   - Mostrar suma de pasajeros: Consulta la suma total de pasajeros en una estación específica para una fecha seleccionada.
   - Modificar registro: Permite modificar datos asociados a una estación.
   - Eliminar registro: Elimina un registro específico de la base de datos.

5. **Resultado**:
   La información se muestra mediante mensajes emergentes o se ejecuta la acción correspondiente en la base de datos.

## Funcionalidades principales

- **Consulta de datos**:
  Utilizando la clase `Estacion` y consultas SQL, se obtienen registros relacionados con estaciones y líneas.

- **Interfaz gráfica**:
  - `Tkinter` para botones, menús desplegables y un calendario interactivo.
  - Mensajes de error y notificaciones.

- **Gestión de base de datos**:
  - Integración con MySQL para acceder a base de datos.

## Contribuir

1. Haz un fork del proyecto.
2. Crea una rama nueva: `git checkout -b mi-nueva-funcionalidad`.
3. Realiza cambios y haz commits: `git commit -m "Agrego nueva funcionalidad"`.
4. Envía un pull request.

## Licencia

Este proyecto está distribuido bajo la licencia MIT, una licencia de software libre y de código abierto que permite:

    Uso: Puedes usar este proyecto en cualquier aplicación, ya sea personal o comercial.
    Distribución: Puedes compartir el proyecto con otros, incluso como parte de tus propios productos.
    Modificación: Puedes modificar el código para adaptarlo a tus necesidades o mejorarlo.
    Sub-licencia: Puedes integrar este código en otros proyectos y redistribuirlo bajo una licencia diferente, si así lo prefieres.
  **Condiciones**
    Crédito: Debes incluir una copia de la licencia original en cualquier distribución o derivado del código, reconociendo al autor original.
    Sin garantías: Este proyecto se proporciona "tal cual", sin garantías de ningún tipo. El autor no se responsabiliza por problemas que puedan surgir del uso del código.
    
## Créditos

- **Desarrolladores**: Tomas Nisenbom, Julian Brianza, Facundo Montivero y Tiziana Arias
- Librerías y tecnologías utilizadas:
  - `Tkinter`
  - `tkcalendar`
  - `mysql.connector`
