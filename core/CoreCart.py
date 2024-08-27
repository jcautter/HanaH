import flet as ft

from core.Core import Core
from core.CoreClientSearch import CoreClientSearch
from core.CoreCartOrder import CoreCartOrder

from data_model.DataModelCart import DataModelCart

class CoreCart(Core, ft.Column):
    def __init__(self, page:ft.Page):
        Core.__init__(self, page)
        ft.Column.__init__(
            self
            , expand=True
            , spacing=10 
            , scroll=ft.ScrollMode.AUTO
        )
        self._build()

    def _build(self):
        self._build_cart_items()
        self._build_control_btn()
        self.controls.append(
            self._cart_items
        )
        self.controls.append(
            CoreClientSearch(self.page___)
        )
        self.controls.append(
            self._control_btn
        )

    def _build_cart_items(self):
        self._cart_items = ft.Column(
            spacing=10
            # , expand=True
        )
        if self.page___.session.contains_key('cart'):
            data_cart = DataModelCart(**self.page___.session.get('cart'))

        for order in data_cart._get('list'):
            self._add_item(
                CoreCartOrder(
                    self.page___
                    , self
                    , order
                )
            )

    def _build_control_btn(self):
        self._control_btn:ft.Row = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
        self._total_button:ft.OutlinedButton = ft.OutlinedButton(
            text='R$ 0.00'
            , width=200 
        )
        self._control_btn.controls.append(self._total_button)
        self._control_btn.controls.append(
            ft.Container(
                content=ft.ElevatedButton(
                    text="Enviar Pedido a Cozinha"
                    ,  icon="send"
                    , color=ft.colors.GREEN_500
                )
                , alignment=ft.alignment.bottom_right
                # , expand=True
            )
        )

    def _add_item(self, item:CoreCartOrder):
        self._cart_items.controls.append(item)

    def _remove_item(self, item:CoreCartOrder):
        self._cart_items.controls.remove(item)
        self.page___.update()

    def _update_cart_on_session(self, order, remove:bool=False):
        if self.page___.session.contains_key('cart'):
            data_cart = DataModelCart(**self.page___.session.get('cart'))
        list_order = data_cart._get('list')
        if not remove:
            list_order = [order if o._get('_id') == order._get('_id') else o for o in list_order]
        else:
            list_order = [order for o in list_order if o._get('_id') == order._get('_id')]
        data_cart._set('list', list_order)
        self.page___.session.set('cart', data_cart._get_dict())

    def _update_total(self):
        if self.page___.session.contains_key('cart'):
            cart = DataModelCart(**self.page___.session.get('cart'))
        total = 0
        for o in cart._get('list'):
            total += o._get('quantity') * o._get('product')._get('value')
        self._total_button.text = f"R$ {total:.2f}"
        self.page___.update()