import flet as ft

from config.common import (Route, Language, Terms)

from meta_class.data_model.DataModelProduct import DataModelProduct

class ProductCatalog(ft.Card):
    def __init__(
            self, page, product:DataModelProduct, btn_action=None, img_size:tuple=(150,150)
        ):
        self._props = {
            'product': product
            , 'btn_action': btn_action
            , 'img_size': img_size

            # 'img_path': img_path
            # , 'name': name
            # , 'short_description': short_description
            # , 'value': "R$ {val:.2f}".format(val=value)
            # , 'btn_text': btn_text
            # , 'btn_action': btn_action
            # , 'img_size': img_size
        }
        super().__init__()
        self.___page = page

        self._buildImage()
        self._buildContainerData()
        
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

    def _get_lang(self):
        return self.___page.client_storage.get("user")['lang']
    
    def _go_order(self, e):
        self.___page.session.set("product", self._props['product']._get_dict())
        self._props['btn_action'](e, Route.ORDER)

    def _buildImage(self):
        self._img = ft.Image(
            src=self._props['product']._get('img_path')
            , width=self._props['img_size'][0]
            , height=self._props['img_size'][1]
            , fit=ft.ImageFit.FILL
        )
    
    def _buildContainerData(self):
         self._containerData = ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        title=ft.Text(self._props['product']._get('name'))
                        , subtitle=ft.Text(self._props['product']._get('short_description'))
                    ),
                    ft.Row(
                        [
                            ft.Container(
                                content=ft.Text("R$ {val:.2f}".format(val =self._props['product']._get('value')), color=ft.colors.BLUE_500)
                                , alignment=ft.alignment.center_left
                            )
                            , ft.Container(
                                content=ft.TextButton(
                                    Terms.ASK[self._get_lang()]
                                    , on_click=lambda e: self._go_order(e) #self._props['btn_action'](e, Route.ORDER)
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