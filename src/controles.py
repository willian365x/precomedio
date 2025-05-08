import os
from dotenv import set_key, load_dotenv
import flet as ft

load_dotenv()


class Calculo(ft.BottomSheet):
    def __init__(self):
        self.__field_quantidade = ft.TextField(
            label='Quantidade',
            keyboard_type=ft.KeyboardType.NUMBER,
            prefix_icon=ft.Icon(ft.Icons.NUMBERS, color='green'),
            border_radius=8,
        )
        self.__field_preco = ft.TextField(
            label='Preço',
            keyboard_type=ft.KeyboardType.NUMBER,
            prefix_icon=ft.Icon(ft.Icons.MONEY, color='green'),
            prefix_text='R$',
            border_radius=8,
        )
        self.__button_gravar = ft.ElevatedButton('Gravar',
                                                 icon=ft.Icons.SAVE,
                                                 on_click=lambda e: self.on_click_gravar()
                                                 )

        self.__button_limpar = ft.ElevatedButton('Limpar',
                                                 icon=ft.Icons.CLEAR,
                                                 on_click=lambda e: self.on_click_clear()
                                                 )

        self.__content = \
            ft.Container(
                ft.Column(
                    [
                        self.__field_quantidade,
                        self.__field_preco,
                        ft.Row(
                            [
                                self.__button_gravar,
                                self.__button_limpar
                            ],
                        ),
                    ],
                    tight=True,
                ),
                padding=30,
            )
        super().__init__(content=self.__content)

    def on_click_clear(self):
        self.__field_quantidade.value = None
        self.__field_preco.value = None
        self.update()

    def on_click_gravar(self):
        try:
            quantidade = str(self.__field_quantidade.value)
            preco = str(self.__field_preco.value)

            env_path = '.env'

            set_key(env_path, 'QUANTIDADE', quantidade)
            set_key(env_path, 'PRECO', preco)

            dlg_success = ft.AlertDialog(
                title=ft.Text('Sucesso'),
                icon=ft.Icon(ft.Icons.ABC),
                content=ft.Text('Dados registrados com sucesso!'),
                actions=[
                    ft.TextButton(
                        'Ok', on_click=lambda e: self.page.close(dlg_success))
                ],
                actions_alignment=ft.MainAxisAlignment.CENTER,
                on_dismiss=lambda e: print("Alert Dialog foi fechado")
            )

            os.environ['QUANTIDADE'] = quantidade
            os.environ['PRECO'] = preco

            self.page.open(dlg_success)

        except Exception as e:
            print(e)
        finally:
            self.page.close(self)
