import flet as ft

from core.Core import Core
from core.CoreCart import CoreCart

class ViewCart(Core, ft.View):
    def __init__(self, page:ft.Page):
        Core.__init__(self, page)
        route = self.ROUTE.CART
        ft.View.__init__(self, route=route)
        self.expand = True
        self._build()

    def _build(self):
        self._build_controls()
        self._build_appbar()

    def _build_controls(self):
        self.controls = [
            CoreCart(self.page___)
        ]


    def _build_appbar(self):
        self.appbar = ft.AppBar(
            title=ft.Text(self.TERMS.CART[self._get_lang()])
            , bgcolor=ft.colors.SURFACE_VARIANT
        )