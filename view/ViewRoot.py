import flet as ft

from core.Core import Core

from core.CoreCatalog import CoreCatalog
from core.CoreCatalogMenu import CoreCatalogMenu
from core.CoreCatalogProduct import CoreCatalogProduct

from data_model.DataModelCatalog import DataModelCatalog

class ViewRoot(
    Core
    , ft.View
    ):
    def __init__(self, page:ft.Page):
        Core.__init__(self, page)
        ft.View.__init__(self)
        self.route = self.ROUTE.ROOT
        self._buid()

    def _buid(self):
        self._build_controls()
        self._build_draer()
        self._build_navigation_bar()
        self._build_appbar()

    def _page_go_from_navigation_bar(self, e, route):
        e.page.go(route)

    def _build_controls(self):
        catalog = CoreCatalog(self.page___)
        menu = CoreCatalogMenu(self.page___, catalog)
        
        category = None
        data_catalog = DataModelCatalog()
        for product in data_catalog._get('list'):
            if category != product._get('category'):
                category = product._get('category')
                menu._add_item(category)
                catalog._add_title(category)

            catalog._add_item(
                CoreCatalogProduct(
                    **{
                        'page': self.page___
                        , 'product': product
                        , 'btn_action': self._page_go_from_navigation_bar
                    }
                )
            )
        self.controls = [
            menu
            , catalog
        ]   

    def _build_appbar(self):
        self.appbar = ft.AppBar(
            title=ft.Text("Flet app 2")
            , bgcolor=ft.colors.SURFACE_VARIANT
        )

    def _page_go_from_drawer(self, e, route):
        e.page.go(route)

    def _build_draer(self):
        self.drawer = ft.NavigationDrawer(
            open=False,
            controls=[
                ft.FilledTonalButton(
                    "Visit Store"
                    , icon=ft.icons.STORE
                    , on_click=lambda e: self._page_go_from_drawer(e, self.ROUTE.STORE)
                )
                , ft.FilledTonalButton(
                    "Nova View"
                    , icon=ft.icons.STACKED_BAR_CHART
                     , on_click=lambda e: self._page_go_from_drawer(e, self.ROUTE.NOVAVIEW)
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
                        , label=self.TERMS.CATALOG[self._get_lang()]
                )
                , ft.NavigationBarDestination(
                    icon=ft.icons.BOOKMARK_OUTLINE
                    , selected_icon=ft.icons.BOOKMARK
                    , label=self.TERMS.ORDERS[self._get_lang()]
                )
                , ft.NavigationBarDestination(
                    icon=ft.icons.AIRPORT_SHUTTLE_OUTLINED
                    , selected_icon=ft.icons.AIRPORT_SHUTTLE
                    , label=self.TERMS.ORDERS_READY[self._get_lang()]
                )
            ]
        )