import flet as ft

from core.Core import Core

class ViewStore(Core, ft.View):
    def __init__(self, page):
        Core.__init__(self, page)
        ft.View.__init__(self)
        self.route = self.ROUTE.STORE
        self._build()

    def _build(self):
        self._build_controls()
        self._build_appbar()

    def _build_controls(self):

        total_text = ft.Text(f"Total: R$ 30.50", weight="bold")

        total_button = ft.OutlinedButton(
            text=f"Valor Total: R$ 30.50",
            width=200,
        )

        self.controls = [
            ft.Column(
                controls=[
                    ft.Column(
                        controls=[
                            ft.Column(
                                controls=None
                                , spacing=10
                            )
                            , total_text
                        ]
                        , spacing=10
                        , expand=True
                    ),
                    ft.Row(
                        controls=[
                            total_button,
                            ft.Container(
                                content=ft.ElevatedButton(
                                    text="Enviar Pedido a Cozinha", 
                                    icon="send", 
                                    color=ft.colors.GREEN_500
                                ),
                                alignment=ft.alignment.bottom_right,
                                expand=True
                            )
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    )
                ]
                , expand=True
            )
        ]

    def _build_appbar(self):
        self.appbar = ft.AppBar(
            title=ft.Text("Store")
            , bgcolor=ft.colors.SURFACE_VARIANT
        )