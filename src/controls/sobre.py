import flet as ft


class Sobre(ft.AlertDialog):
    def __init__(self, modal: bool = False):
        super().__init__(modal=modal)
        self.icon = ft.Icon(ft.Icons.MESSAGE)
        self.title = ft.Text('Preço Médio')
        self.content = ft.Container(
            ft.Column(
            [
                ft.Text('Versão: 0.0.1'),
                ft.Text('Developer: Willian Silva'),
                ft.Text('Contato: @willian365x'),
                ft.Divider(height=10),
            ],
            alignment=ft.CrossAxisAlignment.CENTER
            ),
            height=100,
        )
        self.alignment = ft.alignment.center
        self.actions = [
            ft.TextButton('Ok', on_click=lambda e: ft.Page.close(self))
        ]

        
