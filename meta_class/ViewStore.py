import flet as ft

class ViewStore(ft.View):
    def __init__(self):
        route = '/store'
        super().__init__(route=route)
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
            title=ft.Text("Store")
            , bgcolor=ft.colors.SURFACE_VARIANT
        )