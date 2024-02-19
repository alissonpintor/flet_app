import flet as ft


def main(page: ft.Page):
    img = ft.Image(
        src='https://assets.xboxservices.com/assets/f2/09/f2093a9f-81ef-4ddd-9128-7e409ab3e6ad.jpg?n=Red-Dead-Redemption-II_GLP-Page-Hero-1084_1920x1080.jpg',
        border_radius=ft.border_radius.all(25),
        height=1000,
        width=200,
        rotate=ft.Rotate(0),
        fit=ft.ImageFit.CONTAIN,
        repeat=ft.ImageRepeat.REPEAT_Y
    )

    page.add(img)


if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')