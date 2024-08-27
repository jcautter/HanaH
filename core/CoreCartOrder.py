import flet as ft

from core.Core import Core

from data_model.DataModelCart import DataModelCart
from data_model.DataModelOrder import DataModelOrder

class CoreCartOrder(Core, ft.Container):

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
            self._props['cart']._update_cart_on_session(self._props['order'])
            self._total_quantity.value = str(self._props['order']._get('quantity'))
            self._total_text.value = f"R$ {self._props['order']._get('product')._get('value') * self._props['order']._get('quantity'):.2f}"
            self._props['cart']._update_total()
            self.page___.update()
        else:
            self._zero_out_item()

    def _zero_out_item(self):
        self._props['cart']._update_cart_on_session(self._props['order'], remove=True)
        self._props['cart']._update_total()
        self._props['cart']._remove_item(self)
        self.page___.update()

    def _build(self):
        self._total_text:ft.Text = ft.Text(
            f"R$ {self._props['order']._get('product')._get('value') * self._props['order']._get('quantity'):.2f}"
        )
        self._total_quantity:ft.Text = ft.Text(
            str(self._props['order']._get('quantity'))
        )
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