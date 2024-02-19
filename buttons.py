import flet as ft


def main(page: ft.Page):
    page.window_width = 400
    page.spacing = 15

    btn1 = ft.ElevatedButton(text='Clique aqui')
    btn2 = ft.ElevatedButton(text='Botão inativo', disabled=True)
    btn3 = ft.ElevatedButton(text='Botão com icone', icon=ft.icons.HOME)
    btn4 = ft.ElevatedButton(
        text='Demais propriedades',
        bgcolor=ft.colors.AMBER,
        color=ft.colors.RED,
        icon=ft.icons.FAVORITE,
        icon_color=ft.colors.CYAN
    )

    btn_style = ft.ButtonStyle(
        color={
            ft.MaterialState.HOVERED: ft.colors.CYAN,
            ft.MaterialState.DEFAULT: ft.colors.AMBER
        },
        bgcolor={
            ft.MaterialState.HOVERED: ft.colors.AMBER
        },
        padding={
            ft.MaterialState.DEFAULT: ft.padding.symmetric(vertical=10, horizontal=20),
            ft.MaterialState.HOVERED: ft.padding.symmetric(vertical=20, horizontal=40)
        },
        side={
            ft.MaterialState.DEFAULT: ft.BorderSide(width=0.5, color=ft.colors.WHITE),
            ft.MaterialState.HOVERED: ft.BorderSide(width=1, color=ft.colors.RED)
        },
        shape={
            ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=10)
        },
        animation_duration=1000
    )
    btn5 = ft.ElevatedButton(
        text='Botão com estilo personalizado',
        style=btn_style
    )

    def btn_clicked(e):
        e.control.data += 1
        text.value = f'O botão foi clicado {e.control.data} vezes'
        page.update()

    btn6 = ft.ElevatedButton(
        text='Incrementar',
        style=btn_style,
        on_click=btn_clicked,
        data=0
    )

    text = ft.Text()

    page.add(btn1,btn2, btn3, btn4, btn5, btn6, text)


if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')