# Clase Estacion
class Estacion:
    def __init__(self, nombre, linea):
        self.__nombre = nombre
        self.__linea = linea

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nuevoNombre):
        self.__nombre = nuevoNombre

    def get_linea(self):
        return self.__linea

    def set_linea(self, nuevaLinea):
        self.__linea = nuevaLinea
        
    def buscar_estacion(self, cursor):
            # Utilizar parámetros para evitar inyección SQL
            query = "SELECT * FROM Estaciones WHERE nombre = %s AND linea = %s"
            cursor.execute(query, (self.get_nombre(), self.get_linea()))
            result = cursor.fetchone()
            
            if result:
                nombre = result[2]  # Tercera columna: 'nombre'
                linea = result[3]   # Cuarta columna: 'linea'
                return (nombre, linea)
            else:
                return None  # Si no se encuentra la estación, devuelve None