import flet as ft
import time

def main(page: ft.Page):

    def button_clicked(e):
        page.add(ft.Text('Clicked!'))

    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    t = ft.Text(value='Hello, world', color='green')

    page.controls.append(t)
    page.update()

    for i in range(10):
        t.value = f'Step {i}'
        page.update()
        time.sleep(0.1)
    
    page.add(
        ft.Row(controls=[
            ft.Text('A'),
            ft.Text('B'),
            ft.Text('C')
        ])
    )

    page.add(
        ft.Row(controls=[
            ft.TextField(label="Your name"),
            ft.ElevatedButton(text="Click me!", on_click=button_clicked)
        ])
    )
    page.update()

    def add_clicked(e):
        if new_task.value:
            page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        new_task.focus()
        new_task.update()

    new_task = ft.TextField(hint_text="Whats needs to be done?", width=300, prefix_icon=ft.icons.SEARCH)
    page.add(ft.Row([new_task, ft.ElevatedButton("Add", on_click=add_clicked)]))


ft.app(port=8000, target=main)