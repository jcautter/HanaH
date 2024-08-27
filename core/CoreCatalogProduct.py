import flet as ft

from core.Core import Core

from data_model.DataModelProduct import DataModelProduct

class CoreCatalogProduct(Core, ft.Card):
    def __init__(self, page, product:DataModelProduct, btn_action=None, img_size:tuple=(150,150)):
        self._props = {
            'product': product
            , 'btn_action': btn_action
            , 'img_size': img_size
        }
        Core.__init__(self, page)
        ft.Card.__init__(self)
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
    
    def _go_order(self, e):
        self.___page.session.set("product", self._props['product']._get_dict())
        self._props['btn_action'](e, self.ROUTE.ORDER)

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
                                content=ft.Text(
                                    "R$ {val:.2f}".format(
                                        val = self._props['product']._get('value')
                                    )
                                    , color=ft.colors.BLUE_500
                                )
                                , alignment=ft.alignment.bottom_left
                            )
                            , ft.Container(
                                content=ft.TextButton(
                                    self.TERMS.ASK[self._get_lang()]
                                    , on_click=lambda e: self._go_order(e)
                                )
                                , alignment=ft.alignment.bottom_center
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