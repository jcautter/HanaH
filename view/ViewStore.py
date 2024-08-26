import flet as ft

from core.Core import Core

class ViewStore(Core, ft.View):
    def __init__(self, page):
        Core.__init__(self, page)
        ft.View.__init__(self)
        self.route = self.ROUTE.STORE
        self._buid()

    def _buid(self):
        self._build_controls()
        self._build_appbar()

    def _build_controls(self):
        self.controls = [
            ft.ElevatedButton(
                "Go Home"
                , on_click=lambda e: self._view_pop()
            )
        ]

    def _build_appbar(self):
        self.appbar = ft.AppBar(
            title=ft.Text("Store")
            , bgcolor=ft.colors.SURFACE_VARIANT
        )