import flet as ft

def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(
        value="10", 
        text_align=ft.TextAlign.RIGHT,
        width=100, 
        label='Contador',
        color='#acabed',
        bgcolor='#0c09b8',
        border_radius=10,
        border_color='#5351c9'
    )

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )
    )

ft.app(target=main)