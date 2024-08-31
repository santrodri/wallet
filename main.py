import flet as ft
from tkinter.filedialog import asksaveasfilename

from controller import exec

def ask_save() -> str:
    types = [('Text Document', '*.txt')]
    return asksaveasfilename(filetypes=types, defaultextension='.txt')

def create_virtual_wallet():
    data: dict = exec.create_wallet()
    path: str = ask_save()
    
    if path is None: return 

    with open(path, mode='+w') as data_path:
        for k, v in data.items():
            data_path.write(f'{k}: {v}\n')


def main(page: ft.Page):
    page.title = "Dominus"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_height = 400
    page.window_width = 400

    main_text = ft.Text('Crie sua carteira bitcoin com facilidade')
    button = ft.IconButton(ft.icons.SEND, on_click=lambda e: create_virtual_wallet())

    page.add(
        ft.Row(
            [
              main_text ,
              button
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(main)