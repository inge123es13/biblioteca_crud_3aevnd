from dao.libro_dao import LibroDAO
from models.libro import Libro


def ver_todo(libro_dao):
    try:
        libros = libro_dao.obtener_libros()

        print("\nLibros en la biblioteca")

        if len(libros) == 0:
            print("No hay libros registrados")
        else:
            for libro in libros:
                print(f"{libro.id_libro} - {libro.titulo} - {libro.autor} - {libro.isbn} - {libro.disponible}")

        print("\nConexión exitosa a la base de datos")

    except Exception as e:
        print(f"Error al conectar la base de datos: {e}")


def insertar_libro(libro_dao):
    try:
        print("--------------------------------------------------------")
        print("Inserción de un nuevo libro")

        id_libro = int(input("Escribe el ID del libro: "))
        titulo = input("Escribe título del libro: ")
        autor = int(input("Escribe el id del autor: "))
        isbn = input("Escribe el ISBN del libro: ")
        disponible = True

        nuevo_libro = Libro(id_libro, titulo, autor, isbn, disponible)
        libro_dao.insertar(nuevo_libro)

        print("Libro insertado correctamente")

    except Exception as e:
        print(f"Error al insertar el libro: {e}")


def actualizar_libro(libro_dao):
    try:
        ver_todo(libro_dao)

        id_libro = int(input("Escribe el ID del libro a editar: "))

        print("Actualiza los datos de este libro")
        titulo = input("Escribe el nuevo título del libro: ")
        autor = int(input("Escribe el nuevo id del autor: "))
        isbn = input("Escribe el nuevo ISBN del libro: ")

        respuesta = input("¿Está disponible? (s/n): ").lower()
        disponible = respuesta == "s"

        libro = Libro(id_libro, titulo, autor, isbn, disponible)
        libro_dao.actualizar(libro)

        print("Libro actualizado correctamente")

    except Exception as e:
        print(f"Error al actualizar el libro: {e}")


def eliminar_libro(libro_dao):
    try:
        ver_todo(libro_dao)

        id_libro = int(input("Escribe el ID del libro a eliminar: "))
        libro_dao.eliminar(id_libro)

        print("Libro eliminado correctamente")
        ver_todo(libro_dao)

    except Exception as e:
        print(f"Error al eliminar el libro: {e}")


def main():
    libro_dao = LibroDAO()

    print("=== Biblioteca Universitaria ===")
    print("1. Ver todos los libros")
    print("2. Insertar nuevo libro")
    print("3. Actualizar un libro existente")
    print("4. Eliminar un libro existente")

    opcion = int(input("Escribe una opción (1-4): "))

    match opcion:
        case 1:
            ver_todo(libro_dao)
        case 2:
            insertar_libro(libro_dao)
        case 3:
            actualizar_libro(libro_dao)
        case 4:
            eliminar_libro(libro_dao)
        case _:
            print("Opción no válida")


if __name__ == "__main__":
    main()