import flet as ft
from ui.libro_form import libro_form
from ui.libros_list import libros_list


def main_window(page: ft.Page):

    page.title = "Sistema de gestión de Biblioteca"
    page.window.width = 1100
    page.window.height = 700
    page.padding = 0
    page.bgcolor = ft.Colors.BLUE_GREY_50

    titulo = ft.Text(
        "Sistema de Gestión de Biblioteca",
        size=24,
        weight=ft.FontWeight.BOLD
    )

    subtitulo = ft.Text(
        "Seleccione una opción del menú",
        size=16,
        color=ft.Colors.BLUE_GREY_600
    )

    contenido = ft.Container(
        padding=30,
        expand=True
    )

    def inicio():
        return ft.Column(
            controls=[
                titulo,
                subtitulo
            ],
            spacing=10
        )

    def mostrar_inicio(e=None):
        contenido.content = inicio()
        page.update()

    def mostrar_insertar_libro(e=None):
        contenido.content = libro_form(mostrar_inicio)
        page.update()

    def mostrar_lista_libros(e=None):
        contenido.content = libros_list(mostrar_inicio)
        page.update()

    

    menu_lateral = ft.Container(
        width=220,
        bgcolor=ft.Colors.BLUE_GREY_900,
        padding=20,
        content=ft.Column(
            controls=[
                ft.Text(
                    "Biblioteca",
                    size=22,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE
                ),

                ft.Text(
                    "Sistema de Gestión",
                    size=12,
                    color=ft.Colors.BLUE_GREY_100
                ),

                ft.Divider(
                    color=ft.Colors.BLUE_GREY_700
                ),

                ft.ElevatedButton(
                    content=ft.Text("Inicio"),
                    icon=ft.Icons.HOME,
                    width=180,
                    on_click=mostrar_inicio
                ),

                ft.ElevatedButton(
                    content=ft.Text("Libros"),
                    icon=ft.Icons.BOOK,
                    width=180,
                    on_click=mostrar_lista_libros
                ),

                ft.ElevatedButton(
                    content=ft.Text("Usuarios"),
                    icon=ft.Icons.PERSON,
                    width=180
                ),

                ft.ElevatedButton(
                    content=ft.Text("Préstamos"),
                    icon=ft.Icons.SWAP_HORIZ,
                    width=180
                ),

                ft.ElevatedButton(
                    content=ft.Text("Devoluciones"),
                    icon=ft.Icons.KEYBOARD_RETURN,
                    width=180
                ),
            ],
            spacing=15
        )
    )

    layout = ft.Row(
        controls=[
            menu_lateral,
            contenido
        ],
        expand=True,
        spacing=0
    )

    page.add(layout)

    mostrar_inicio()