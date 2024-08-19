import flet as ft

class ItemCardapio(ft.Card):
    def __init__(
            self, name:str, short_description:str, value:float, img_path:str, btn_action=None
            , _id:str=None, description:str=None, category:str=None, btn_text:str='Pedir', img_size:tuple=(150,150)
        ):
        self._props = {
            'img_path': img_path
            , 'name': name
            , 'short_description': short_description
            , 'value': "R$ {val:.2f}".format(val=value)
            , 'btn_text': btn_text
            , 'btn_action': btn_action
            , 'img_size': img_size
        }
        self.buildImage()
        self.buildContainerData()
        super().__init__()

        self.content = ft.Container(
            content=ft.Row(
                [
                    self._img
                    , self._containerData
                ]
                , alignment=ft.MainAxisAlignment.START
            ),
            padding=5
        )

    def buildImage(self):
        self._img = ft.Image(
            src=self._props['img_path']
            , width=self._props['img_size'][0]
            , height=self._props['img_size'][1]
            , fit=ft.ImageFit.FILL
        )
    
    def buildContainerData(self):
         self._containerData = ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        title=ft.Text(self._props['name'])
                        , subtitle=ft.Text(self._props['short_description'])
                    ),
                    ft.Row(
                        [
                            ft.Container(
                                content=ft.Text(self._props['value'], color=ft.colors.BLUE_500)
                                , alignment=ft.alignment.center_left
                            )
                            , ft.Container(
                                content=ft.TextButton(
                                    self._props['btn_text']
                                    , on_click=lambda e: self._props['btn_action'](e, '/pedido')
                                )
                                , alignment=ft.alignment.center_right
                            )
                        ]
                        , alignment = ft.MainAxisAlignment.SPACE_BETWEEN
                    )
                ]
                , alignment=ft.MainAxisAlignment.START
                , spacing=5
            )
            , expand=True
        )