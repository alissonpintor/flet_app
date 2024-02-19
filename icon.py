import flet as ft


def main(page: ft.Page):
    icon = ft.Icon(
        name=ft.icons.FAVORITE,
        color=ft.colors.AMBER,
        size=50
    )

    page.add(icon)


if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')