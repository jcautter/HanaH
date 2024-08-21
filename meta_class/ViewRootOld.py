import flet as ft

class ViewRootOld(ft.View):
    def __init__(self):
        super().__init__()
        self.route = '/'
        self._buid()

    def _buid(self):
        self._build_controls()
        self._build_draer()
        self._build_navigation_bar()
        self._build_appbar()

    def _build_controls(self):
        self.controls = [
            ft.VerticalDivider(width=1)
            , ft.Column([ ft.Text("Body!!!")], alignment=ft.MainAxisAlignment.START, expand=True)
            , ft.ElevatedButton(
                "Visit Store"
                , on_click=lambda e: e.page.go("/store")
            ) 
        ]
    
    def _build_appbar(self):
        self.appbar = ft.AppBar(
            title=ft.Text("Flet app 2")
            , bgcolor=ft.colors.SURFACE_VARIANT
        )
    def _page_go_from_drawer(self, e, route):
        # e.page.close(e.page.views[-1].drawer)
        e.page.go(route)

    def _build_draer(self):
        self.drawer = ft.NavigationDrawer(
            open=False,
            controls=[
                ft.FilledTonalButton(
                    "Visit Store"
                    , icon=ft.icons.STORE
                     , on_click=lambda e: self._page_go_from_drawer(e, "/store")
                )
                , ft.FilledTonalButton(
                    "Nova View"
                    , icon=ft.icons.STACKED_BAR_CHART
                     , on_click=lambda e: self._page_go_from_drawer(e, "/novaview")
                )
                , ft.NavigationDrawerDestination(
                    icon=ft.icons.ADD_TO_HOME_SCREEN_SHARP
                    , label="Visit Store"
                ),
                ft.NavigationDrawerDestination(
                    icon=ft.icons.ADD_COMMENT
                    , label="Item 2"
                ),
            ],
        )

    def _build_navigation_bar(self):
        self.navigation_bar = ft.NavigationBar(
            destinations=[
                ft.NavigationBarDestination(
                        icon=ft.icons.FOOD_BANK_OUTLINED
                        , selected_icon=ft.icons.FOOD_BANK
                        , label="Cardapio"
                )
                , ft.NavigationBarDestination(
                    icon=ft.icons.BOOKMARK_OUTLINE
                    , selected_icon=ft.icons.BOOKMARK
                    , label="Pedidos"
                )
                , ft.NavigationBarDestination(
                    icon=ft.icons.AIRPORT_SHUTTLE_OUTLINED
                    , selected_icon=ft.icons.AIRPORT_SHUTTLE
                    , label="Preparados"
                )
            ]
        )