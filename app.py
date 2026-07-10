import flet as ft

from ui.main_window import main_window
from dao.libro_dao import LibroDAO
from dao.usuario_dao import UsuarioDAO
from models.libro import Libro
from models.usuario import Usuario


# ---------- LIBROS ----------

def ver_libros(libro_dao):
    try:
        libros = libro_dao.obtener_libros()

        print("LIBROS EN LA BIBLIOTECA:")
        if len(libros) == 0:
            print("No hay libros registrados")
        else:
            for libro in libros:
                print(f"{libro.id} - {libro.titulo} - {libro.autor} - {libro.isbn} - {libro.disponible}")

    except Exception as e:
        print(f"Error al consultar libros: {e}")


def insertar_libro(libro_dao):
    try:
        print("Inserccion de un nuevo libro")

        titulo = input("Escribe titulo del libro: ")
        autor = int(input("Escribe el id del autor: "))
        isbn = input("Escribe el ISBN del libro: ")
        disponible = True

        nuevoLibro = Libro(0, titulo, autor, isbn, disponible)
        libro_dao.insertar(nuevoLibro)

        print("Libro insertado correctamente")

    except Exception as e:
        print(f"Error al insertar libro: {e}")


def actualizar_libro(libro_dao):
    ver_libros(libro_dao)

    id = int(input("Escribe el id del libro a editar: "))
    titulo = input("Escribe el nuevo titulo del libro: ")
    autor = int(input("Escribe el nuevo id del autor: "))
    isbn = input("Escribe el nuevo ISBN del libro: ")

    respuesta = input("¿El libro esta disponible? (si/no): ")

    disponible = True if respuesta.lower() == "si" else False

    libro = Libro(id, titulo, autor, isbn, disponible)
    libro_dao.actualizar(libro)

    print("Libro actualizado correctamente")


def eliminar_libro(libro_dao):
    ver_libros(libro_dao)

    id = int(input("Escribe el id del libro a eliminar: "))
    libro_dao.eliminar(id)

    print("Libro eliminado correctamente")


# ---------- USUARIOS ----------

def ver_usuarios(usuario_dao):
    try:
        usuarios = usuario_dao.obtener_usuarios()

        print("USUARIOS EN LA BIBLIOTECA:")
        if len(usuarios) == 0:
            print("No hay usuarios registrados")
        else:
            for usuario in usuarios:
                print(f"{usuario.id} - {usuario.nombre} - {usuario.matricula} - {usuario.carrera} - {usuario.correo} - {usuario.activo}")

    except Exception as e:
        print(f"Error al consultar usuarios: {e}")


def insertar_usuario(usuario_dao):
    try:
        print("Inserccion de un nuevo usuario")

        nombre = input("Escribe el nombre del usuario: ")
        matricula = input("Escribe la matricula del usuario: ")
        carrera = int(input("Escribe el id de la carrera: "))
        correo = input("Escribe el correo del usuario: ")
        activo = True

        nuevoUsuario = Usuario(0, nombre, matricula, carrera, correo, activo)
        usuario_dao.insertar(nuevoUsuario)

        print("Usuario insertado correctamente")

    except Exception as e:
        print(f"Error al insertar usuario: {e}")


def actualizar_usuario(usuario_dao):
    ver_usuarios(usuario_dao)

    id = int(input("Escribe el id del usuario a editar: "))
    nombre = input("Escribe el nuevo nombre del usuario: ")
    matricula = input("Escribe la nueva matricula: ")
    carrera = int(input("Escribe el nuevo id de carrera: "))
    correo = input("Escribe el nuevo correo: ")

    respuesta = input("¿El usuario esta activo? (si/no): ")

    activo = True if respuesta.lower() == "si" else False

    usuario = Usuario(id, nombre, matricula, carrera, correo, activo)
    usuario_dao.actualizar(usuario)

    print("Usuario actualizado correctamente")


def eliminar_usuario(usuario_dao):
    ver_usuarios(usuario_dao)

    id = int(input("Escribe el id del usuario a eliminar: "))
    usuario_dao.eliminar(id)

    print("Usuario eliminado correctamente")


# ---------- MENUS ----------

def menu_libros():
    libro_dao = LibroDAO()

    print("1. Ver todos los libros")
    print("2. Insertar un libro")
    print("3. Actualizar un libro existente")
    print("4. Eliminar un libro existente")

    opcion = int(input("Escribe una opcion (1-4): "))

    match opcion:
        case 1:
            ver_libros(libro_dao)
        case 2:
            insertar_libro(libro_dao)
        case 3:
            actualizar_libro(libro_dao)
        case 4:
            eliminar_libro(libro_dao)


def menu_usuarios():
    usuario_dao = UsuarioDAO()

    print("1. Ver todos los usuarios")
    print("2. Insertar un nuevo usuario")
    print("3. Actualizar un usuario existente")
    print("4. Eliminar un usuario existente")

    opcion = int(input("Escribe una opcion (1-4): "))

    match opcion:
        case 1:
            ver_usuarios(usuario_dao)
        case 2:
            insertar_usuario(usuario_dao)
        case 3:
            actualizar_usuario(usuario_dao)
        case 4:
            eliminar_usuario(usuario_dao)

ft.app( target = main_window)
#def main():
   
    # print("== BIBLIOTECA UNIVERSITARIA ==")
    # print("1. Gestion de libros")
    # print("2. Gestion de usuarios")

    # opcion = int(input("Escribe tu opcion: "))

    # match opcion:
    #     case 1:
    #         menu_libros()
    #     case 2:
    #         menu_usuarios()


    #if __name__ == "__main__":
     # main()