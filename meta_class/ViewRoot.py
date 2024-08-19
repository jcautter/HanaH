import flet as ft

from meta_class.core.Cardapio import Cardapio
from meta_class.core.MenuCardapio import MenuCardapio
from meta_class.core.ItemCardapio import ItemCardapio

from meta_class.data_model.DataModelMenu import DataModelMenu

class ViewRoot(ft.View):
    def __init__(self):
        super().__init__()
        self.route = '/'
        self._buid()

    def _buid(self):
        self._build_controls()
        self._build_draer()
        self._build_navigation_bar()
        self._build_appbar()

    def _page_go_from_navigation_bar(self, e, route):
        print('teste')
        e.page.go(route)

    def _build_controls(self):
        cardapio = Cardapio()
        menu = MenuCardapio(cardapio)
        
        category_txt = None
        data = DataModelMenu()
        for i in data._get('data'):
            if category_txt != i['category']:
                category_txt = i['category']
                menu._add_item(category_txt)
                cardapio._add_title(category_txt)

            cardapio._add_item(
                ItemCardapio(
                    **{
                        **i
                        , 'btn_action': self._page_go_from_navigation_bar
                    }
                )
            )


        # for j in range(10):
        #     txt = 'Bebidas'+str(j)
        #     menu._add_item(txt)
        #     cardapio._add_title(txt)
        #     for i in range(j*10, j*10+10):
        #         cardapio._add_item(
        #             ItemCardapio(
        #                 **{
        #                     'img_path': 'img/Bebida.jpg'
        #                     , 'name': 'Suco de Laranja'+str(i)
        #                     , 'short_description': 'Com ou Sem açúcar'+str(i)
        #                     , 'value': 40+i
        #                     , 'btn_action': self._page_go_from_navigation_bar
        #                 }
        #             )
        #         )



        self.controls = [
            menu
            , cardapio
        ]    
        # self.controls = [
        #     ft.VerticalDivider(width=1)
        #     , ft.Column([ ft.Text("Body!!!")], alignment=ft.MainAxisAlignment.START, expand=True)
        #     , ft.ElevatedButton(
        #         "Visit Store"
        #         , on_click=lambda e: e.page.go("/store")
        #     ) 
        # ]
    
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