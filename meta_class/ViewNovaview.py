import flet as ft

from config.common import (Route, Language, Terms)

class ViewNovaview(ft.View):
    def __init__(self, page):
        route = '/novaview'
        super().__init__(route=route)
        self.___page = page
        self._buid()

    def _buid(self):
        self._build_controls()
        self._build_appbar()

    def _build_controls(self):
        self.controls = [
            ft.ElevatedButton(
                "Go Home"
                , on_click=lambda e: e.page.go("/")
            )
        ]

    def _build_appbar(self):
        self.appbar = ft.AppBar(
            title=ft.Text("Nova View")
            , bgcolor=ft.colors.SURFACE_VARIANT
        )