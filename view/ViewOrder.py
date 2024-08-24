import flet as ft

from core.Core import Core

from core.CoreOrder import CoreOrder

class ViewOrder(Core, ft.View):
    def __init__(self, page:ft.Page):
        Core.__init__(self, page)
        route = self.ROUTE.ORDER
        ft.View.__init__(self, route=route)
        self._buid()
    
    def _buid(self):
        self._build_controls()
        self._build_appbar()

    def _build_controls(self):
        pedido = CoreOrder(page = self.page___)
        self.controls = [
            pedido
        ]
    
    def _build_appbar(self):
        self.appbar = ft.AppBar(
            title=ft.Text(self.TERMS.ORDER[self._get_lang()])
            , bgcolor=ft.colors.SURFACE_VARIANT
        )