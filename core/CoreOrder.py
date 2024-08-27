import flet as ft

from core.Core import Core

from data_model.DataModelOrder import DataModelOrder
from data_model.DataModelWaiter import DataModelWaiter
from data_model.DataModelCart import DataModelCart

from datetime import datetime

class CoreOrder(Core, ft.Container):

    def __init__(self, page:ft.Page, quantity:int=1, img_size:tuple=(None,200)):
        Core.__init__(self, page)
        ft.Container.__init__(self)
        order:DataModelOrder = DataModelOrder(
            **{
                '_id': datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                , 'product': self.page___.session.get('product')
                , 'quantity': quantity
                , 'waiter': DataModelWaiter(
                    login=self.page___.client_storage.get("user")['login']
                )
            }
        )
        self._props = {
            'order': order
            , 'img_size': img_size
        }
        self._build()
    
    def _build(self):
        self._build_cover()
        self._build_title()
        self._build_description()
        self._bulid_bottom()

        self.content = ft.Column(
            [
                 self._cover
                 , self._title
                 , self._description
                #  , ft.Container(expand=True)
                 , self._bottom
            ]
        )

    def _go_back(self, e):
            print("Voltar")
            print(e.page.title)
            # self._view_pop()

    def _update_quantity(self, e, change):
            if self._props['order']._get('quantity') + change < 1:
                self._props['order']._set('quantity', 1)
            else:
                self._props['order']._set(
                     'quantity'
                     , self._props['order']._get('quantity') + change
                )
            
            self._quantity.value = str(self._props['order']._get('quantity'))
            self._total.value = f"R${self._props['order']._get('product')._get('value') * self._props['order']._get('quantity'):.2f}"
            e.page.update()

    def _build_cover(self):
        self._cover = ft.Container(
            bgcolor=ft.colors.BLACK
            , content=ft.Stack(
                alignment=ft.Alignment(0, -1)
                , controls=[
                    ft.Image(
                        src=self._props['order']._get('product')._get('img_path')
                        , height=self._props['img_size'][1] # 200
                        , fit=ft.ImageFit.COVER
                    ),
                    ft.Container(
                        content=ft.IconButton(
                            ft.icons.CLOSE 
                            , on_click=self._go_back 
                            , icon_size=30
                            , style=ft.ButtonStyle(shape=ft.CircleBorder())
                            , bgcolor=ft.colors.WHITE                            
                        ),
                        alignment=ft.Alignment(1,0),
                        margin=10
                    ),
                ]
            )
        )

    def _build_title(self):
        self._title = ft.Text(
            self._props['order']._get('product')._get('name'),
            style="headlineLarge",
            text_align=ft.TextAlign.LEFT,
        )

    def _build_description(self):
        self._description = ft.Text(
            self._props['order']._get('product')._get('description'),
            style="bodyMedium",
            text_align=ft.TextAlign.LEFT,
        )

    def _build_quanty(self):
        self._quantity = ft.Text(
            value=str(self._props['order']._get('quantity'))
            # , style="headlineMedium"
        )
    
    def _build_quantity_control(self):
        self._quantity_control = ft.Row(
            controls=[
                ft.IconButton(ft.icons.REMOVE, on_click=lambda e: self._update_quantity(e, -1))
                , self._quantity
                , ft.IconButton(ft.icons.ADD, on_click=lambda e: self._update_quantity(e, 1))
            ]
            # , alignment=ft.MainAxisAlignment.START
            # , spacing=5
        )

    def _build_total(self):
        self._total = ft.Text(
            "R$ {val:.2f}".format(
                val = (
                    self._props['order']._get('product')._get('value') 
                    * self._props['order']._get('quantity')
                )
            )
            , style="bodyMedium"
        )

    def _bulid_bottom(self):
        self._build_quanty()
        self._build_quantity_control()
        self._build_total()
        
        self._bottom = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            , spacing=10
            , controls = [
                 self._quantity_control
                , self._total
                , ft.ElevatedButton(
                    text=self.TERMS.ADD_CART[self._get_lang()]
                    , on_click=lambda e: self._add_cart(e)
                    , style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=8)
                    )
                )
            ]
        )

    def _add_cart(self, e):
        cart = DataModelCart()
        if self.page___.session.contains_key('cart'):
            cart = DataModelCart(**self.page___.session.get('cart'))
        cart._append('list', self._props['order'])
        self.page___.session.set('cart', cart._get_dict())
        self._view_pop()