import flet as ft


def main(page: ft.Page):
    page.fonts = {
        'Roboto': 'fonts/Roboto-Regular.ttf',
        'RobotoBold': 'fonts/Roboto-Bold.ttf'
    }

    t1 = ft.Text(
        value='Meu nome é Alisson',
        theme_style=ft.TextThemeStyle.DISPLAY_LARGE,
        bgcolor=ft.colors.AMBER,
        color=ft.colors.CYAN,
        font_family='RobotoBold',
        italic=True,
        size=30,
        weight=500
    )

    link_style = ft.TextStyle(
        color=ft.colors.BLUE,
        decoration=ft.TextDecoration.UNDERLINE,
        size=30
    )

    title_style = ft.TextStyle(
        color=ft.colors.RED,
        bgcolor=ft.colors.AMBER,
        size=50
    )

    t2 = ft.Text(
        spans=[
            ft.TextSpan(text='Texto com link ', style=link_style, url='https://www.google.com.br'),
            ft.TextSpan(text='continuação do texto... '),
            ft.TextSpan(text='Texto em destaque', style=title_style)
        ],
        size=30
    )

    page.add(t1, t2)


if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')