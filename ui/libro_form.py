import flet as ft

def libro_form(regresar):
    titulo_input = ft.TextField(
        label= "Titulo del libro: ",
        width=400
    )
    autor_input = ft.TextField(
        label= "Autor: ",
        width=400
    )

    isbn_input = ft.TextField(
        label= "ISBN: ",
        width=400
    )

    mensaje= ft.Text(
        "",
        color= ft.Colors.GREEN
    )
#Recupera los valores de los Textfield
    def guardar_libro(e):
        titulo = titulo_input.value
        autor = autor_input.value
        isbn = isbn_input.value

        #Validacion
        if titulo == "" or autor == "" or isbn == "":
            mensaje.value = "Todos los cambios son obligatorios"
            mensaje.color = ft.Colors.RED
        else:
            mensaje.value = f"Libro '{titulo}' guardado correctamente"
            mensaje.color= ft.Colors.GREEN
            print(F"TITULO: {titulo}, AUTOR: {autor}, ISBN: {isbn}")
            titulo_input.value = ""
            autor_input.value= ""
            isbn_input.value= ""
        e.page.update()

    return ft.Container(
        padding=30,
        content= ft.Column(
            controls=[
                ft.Text(
                    "Insertar nuevo libro",
                    size=24,
                    weight= ft.FontWeight.BOLD
                ),
                ft.Text(
                    "Captura los datos básicos del libro",
                    size=14,
                    color= ft.Colors.BLUE_GREY_600
                ),

                titulo_input,
                autor_input,
                isbn_input,

                ft.ElevatedButton(
                    "Guardar",
                    icon= ft.Icons.SAVE,
                    on_click= guardar_libro
                ),

                 ft.OutlinedButton(
                    "Regresar",
                    icon= ft.Icons.ARROW_BACK,
                    on_click= lambda e: regresar()
                ),

                
                
                mensaje
            ],
            spacing=15
        )
    )
    