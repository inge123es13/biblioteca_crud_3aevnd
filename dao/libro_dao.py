#data acces objetct es una clase que se encarga de accedera la base de datos y realizar las operaciones

from database.conexion import Conexion
from models.libro import Libro

class LibroDAO:
#Corresponde a select*from libros
    def obtener_librps(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("Select * FROM libros")

        registros = cursor.fetchall()

        libros = []
        for registro in registros:
            libro = Libro(
                id=registro[0],
                titulo=registro[1],
                autor=registros[2],
                isbn=registro[3],
                disponible=registro[4]
            )
            libro.append(libro)
            cursor.close()
            conexion.close()
            return libros
        
    #insert
    def insertar(self,libro):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        INSER INTO libro(titulo, autor, isbn,diponible)
        VALUES (%s,%s,%s,%s)
        """

        cursor.execute(sql,(libro.titulo,libro.autor,libro.isbn,libro.disponible))

        conexion.commit()
        cursor.close()
        conexion.close()


    def actualizar(self,libro):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql="""
               UPDATE libro
               SET titulo = %s, autor= %s,
               isbn=%s, disponible= %s
               WHERE id = %s
            """ 
        cursor.execute(sql,(libro.titulo,libro.autor,libro.isbn,libro.disponible, libro.id))

        conexion.commit()
        cursor.close()
        conexion.close()


    def eliminar(self,id):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("DELETE FROM libro WHERE id = %s", (id))
        conexion.commit()
        cursor.close()
        conexion.close()
    
