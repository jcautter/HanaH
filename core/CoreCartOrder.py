import flet as ft

from core.Core import Core

from data_model.DataModelCart import DataModelCart
from data_model.DataModelOrder import DataModelOrder

class CoreCartOrder(Core, ft.Container):
    _total_text:ft.Text = ft.Text()
    _total_quantity:ft.Text = ft.Text()

    def __init__(self, page:ft.Page, cart, order:DataModelOrder):
        Core.__init__(self, page)
        ft.Container.__init__(
            self
            , padding=10
            , margin=5
            , bgcolor=ft.colors.GREY_800
            , border_radius=8
        )
        self._props = {
            'cart': cart
            , 'order': order
        }
        self._build()

    def _update_quantity(self, delta):
        qtd = max(0, self._props['order']._get('quantity') + delta)
        if qtd > 0:
            self._props['order']._set(
                'quantity'
                , qtd
            )
            self._total_quantity.value = str(self._props['order']._get('quantity'))
            self._total_text.value = f"R$ {self._props['order']._get('product')._get('value') * self._props['order']._get('quantity'):.2f}"
            self._update_total_cart()
            self.page___.update()
        else:
            self._zero_out_item()

    def _zero_out_item(self):
        if self.page___.session.contains_key('cart'):
            data_cart = DataModelCart(**self.page___.session.get('cart'))
        data_cart._set(
            'list'
            , data_cart._get('list').remove(self._props['order'])
        )
        self.page___.session.set('cart', data_cart._get_dict())
        self._update_total_cart()
        self._props['cart']._remove_item(self)
        self.page___.update()

    def _update_total_cart(self):
        if self.page___.session.contains_key('cart'):
            cart = DataModelCart(**self.page___.session.get('cart'))

        total = sum(
            o._get('quantity') * o._get('product')._get('value')
            for o in cart._get('list')
        )
        self._props['cart']._total_button.text = f"R$ {total:.2f}"
        self.page___.update()

    def _build(self):
        self.content = ft.Row(
            controls=[
                ft.Column(
                    controls=[
                        ft.Text(self._props['order']._get('product')._get('name'), weight="bold"),
                        self._total_text,
                    ],
                    expand=True
                ),
                ft.IconButton(
                    icon=ft.icons.REMOVE,
                    on_click=lambda e: self._update_quantity(-1)
                ),
                self._total_quantity,
                ft.IconButton(
                    icon=ft.icons.ADD,
                    on_click=lambda e: self._update_quantity(1)
                ),
                ft.IconButton(
                    icon=ft.icons.DELETE,
                    icon_color=ft.colors.RED,
                    on_click=lambda e: self._zero_out_item()
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )