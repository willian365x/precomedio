import flet as ft

from controls.sobre import Sobre
from controls.doacao import Doacao


def main(page: ft.Page):
    page.title = 'Preço Médio'

    # controles
    # text_msg = ft.Text('Preço Médio', color=ft.Colors.BLUE, size=50)

    # actions

    # View handle

    app_barra = ft.AppBar(
        leading=ft.Icon(ft.Icons.MONETIZATION_ON_OUTLINED,
                        color=ft.Colors.LIGHT_BLUE),
        leading_width=40,
        title=ft.Text('Preço Médio', weight=ft.FontWeight.BOLD,
                      color=ft.Colors.LIGHT_BLUE),
        center_title=True,
        bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
        actions=[
            ft.IconButton(ft.Icons.ADD, tooltip='Adicionar um novo cálculo',
                          icon_color=ft.Colors.LIGHT_BLUE),
            ft.PopupMenuButton(
                icon_color=ft.Colors.LIGHT_BLUE,
                items=[
                    ft.PopupMenuItem('Faça uma doação',
                                     icon=ft.Icons.CARD_GIFTCARD,
                                     on_click=lambda e: page.open(Doacao())),
                    ft.PopupMenuItem("Sobre",
                                     icon=ft.Icons.MESSAGE,
                                     on_click=lambda e: page.open(Sobre()))
                ]
            )
        ]
    )

    page.appbar = app_barra

    page.add(
        ft.SafeArea(
            ft.Container(
                ft.Column(
                    [
                    ]
                )
            )
        )
    )

ft.app(main)
