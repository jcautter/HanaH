import flet as ft

class ItemCardapio(ft.Card):
    def __init__(self, img_path:str, title:str, subtitle:str, description:str, item_value:str, btn_text:str, btn_action=None, img_size:tuple=(150,150)):
        self._props = {
            'img_path': img_path
            , 'title': title
            , 'subtitle': subtitle
            , 'description' : description
            , 'item_value': item_value
            , 'btn_text': btn_text
            , 'btn_action': btn_action
            , 'img_size': img_size
        }
        self.buildImage()
        self.buildContainerData()
        super().__init__()

        self.content = ft.Container(
            content=ft.Row(
                [self._img, self._containerData]
                , alignment=ft.MainAxisAlignment.START
            ),
            padding=5
        )

    def buildImage(self):
        self._img = ft.Image(
            src=self._props['img_path'],
            width=self._props['img_size'][0],
            height=self._props['img_size'][1],
            fit=ft.ImageFit.FILL
        )
    
    def buildContainerData(self):
         self._containerData = ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        title=ft.Text(self._props['title']),
                        subtitle=ft.Text(self._props['subtitle']),
                    ),
                    ft.Row(
                        [
                            ft.Container(
                                content=ft.Text(self._props['item_value'], color=ft.colors.BLUE_500),
                                alignment=ft.alignment.center_left
                            ),
                            ft.Container(
                                content=ft.TextButton(self._props['btn_text']),
                                alignment=ft.alignment.center_right
                            )
                        ]
                        , alignment = ft.MainAxisAlignment.SPACE_BETWEEN
                    )
                ],
                alignment=ft.MainAxisAlignment.START,
                spacing=5
            ),
            expand=True
        )