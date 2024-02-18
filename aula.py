import flet as ft


def main(page: ft.Page):
    page.title = 'Primeiro app'
    page.bgcolor = 'green'
    page.bgcolor = '#b12b12'
    page.bgcolor = ft.colors.RED
    
    # Propriedades da janela
    page.window_always_on_top = True
    page.window_title_bar_hidden = False
    page.window_frameless = False
    page.window_full_screen = False
    page.window_height = 500
    page.window_max_height = 700
    page.window_width = 400
    page.window_max_width = 500
    page.window_resizable = True
    page.window_top = 100
    page.window_movable = True
    page.window_prevent_close = False
    page.window_progress_bar = 1

    print(page.platform)
    
    page.update()

    mensagem = ft.Text(
        value='Olá Mundo'
    )
    page.add(mensagem)

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.padding = ft.padding.symmetric(vertical=50, horizontal=30)
    page.spacing = 15

    page.add(
        ft.Text(value='Meu nome e Alisson'),
        ft.Container(ft.Text(value='Apenas um teste'), bgcolor=ft.colors.BLACK)
    )

    elementos = [
        ft.Text(value='Elemento 01'),
        ft.Text(value='Elemento 02'),
        ft.Text(value='Elemento 03'),
        ft.Text(value='Elemento 04'),
        ft.Text(value='Elemento 05')
    ]

    page.add(*elementos)


""" class App:
    def __init__(self, page: ft.Page) -> None:
        page.title = 'Primeiro app'
        page.update()
 """

if __name__ == '__main__':
    ft.app(target=main, view=ft.WEB_BROWSER)