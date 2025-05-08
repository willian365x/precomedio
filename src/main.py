import os
import flet as ft
from dotenv import load_dotenv

from controles import Calculo

load_dotenv()


def main(page: ft.Page):
    page.title = 'Preço Médio de Ações'

    # Controles
    calculo = Calculo()
    txt_quantidade = ft.Text()
    txt_preco = ft.Text()
    btn_add_calc = ft.ElevatedButton('Adicionar',
                                     icon=ft.Icons.ADD,
                                     on_click=lambda e: page.open(calculo),
                                     )

    # Action
    def on_close_calculo(e):
        load_dotenv(override=True)
        txt_quantidade.value = f"Quantidade: {os.environ.get('QUANTIDADE')}"
        txt_preco.value = f'Preço: {os.environ.get('PRECO')}'
        print('Dialog BootoSheet foi fechado.')
        page.update()

    calculo.on_dismiss = on_close_calculo

    page.add(
        ft.SafeArea(
            ft.Column(
                [
                    btn_add_calc,
                    txt_quantidade,
                    txt_preco
                ]
            )
        )
    )

    page.overlay.append(calculo)
    page.update()


if __name__ == '__main__':
    ft.app(main)
