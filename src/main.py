import flet as ft
from controles import AppBarra, Calculo

def main(page: ft.Page):
    page.title = 'Preço Médio de Ações'
    # Controles
    app_barra = AppBarra('Preço Médio', icon=ft.Icons.CURRENCY_EXCHANGE)
    calculo = Calculo()

    # Action
    page.add(
        ft.SafeArea(
            ft.Column(
                [
                ]
            )
        )
    )

    page.appbar = app_barra
    page.overlay.append(calculo)
    page.update()


if __name__ == '__main__':
    ft.app(main)
