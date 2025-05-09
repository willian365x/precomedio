import os
from dotenv import set_key, load_dotenv
import flet as ft

load_dotenv()

class AppBarra(ft.AppBar):
    def __init__(self,title=None, icon=None):
        super().__init__()
        self.title=ft.Text(title)
        self.leading_width=40
        self.leading=ft.Icon(icon)
        self.actions=[
            ft.IconButton(icon=ft.Icons.ADD,
                          on_click=lambda e: self.page.open(Calculo())),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem('Doação', 
                                     icon=ft.Icons.CURRENCY_EXCHANGE),
                    ft.PopupMenuItem('Sobre',
                                     icon=ft.Icons.QUESTION_ANSWER),
                ]
            )
        ]
#---------------------------------------------------------------------------------
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

        self.__env_path = '.env'

        if not os.path.exists(self.__env_path):
                with open(self.__env_path, 'w') as env_file:
                    env_file.write('QUANTIDADE=\n')
                    env_file.write('PRECO=\n')

    def on_click_clear(self):
        self.__field_quantidade.value = None
        self.__field_preco.value = None
        self.update()

    def on_click_gravar(self):
        try:
            quantidade = str(self.__field_quantidade.value)
            preco = str(self.__field_preco.value)            

            set_key(self.__env_path, 'QUANTIDADE', quantidade)
            set_key(self.__env_path, 'PRECO', preco)

            dlg_success = ft.AlertDialog(
                title=ft.Text('Sucesso'),
                icon=ft.Icon(ft.Icons.MESSAGE),
                content=ft.Text('Dados registrados com sucesso!'),
                actions=[
                    ft.TextButton(
                        'Ok', on_click=lambda e: self.page.close(dlg_success))
                ],
                actions_alignment=ft.MainAxisAlignment.CENTER,
            )
            self.page.open(dlg_success)
        except Exception as e:
            print(e)
        finally:
            self.page.close(self)
