import flet as ft


def main(page: ft.Page):
    page.window_width = 400
    page.spacing = 15

    btn1 = ft.FilledButton(text='Clique aqui')

    page.add(btn1)


if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')