import flet as ft


class Doacao(ft.AlertDialog):
    def __init__(self, modal: bool = False):
        super().__init__(modal=modal)
        self.icon = ft.Icon(ft.Icons.MESSAGE)
        self.title = ft.Text('Doação')
        self.content = ft.Container(
            ft.Column(
                [
                    ft.Divider(height=10),
                    ft.Text('AJUDE-ME a manter esse software'),
                    ft.Text(
                        '...contribua com qualquer valor através da QRCode/Chave PIX abaixo', no_wrap=False),
                    ft.Image(
                        src='qrcode_doacao.jpg',
                        fit=ft.ImageFit.FILL,
                        width=200,
                        height=200
                    ),
                    ft.Text('Chave pix: willian365x@gmail.com'),
                    ft.Divider(height=10),
                ],
                alignment=ft.CrossAxisAlignment.CENTER
            ),
            height=300,
        )
        self.alignment = ft.alignment.center
        self.actions = [
            ft.TextButton('Ok', on_click=lambda e: ft.Page.close(self))
        ]
