import flet as ft

class Teste:
    def __init__(self, page: ft.Page):
        self.page = page
        
        self.page_setup()
        self.nav_bar_setup()
        self.nav_rail_setup()
        self.build()
    
    def page_setup(self):
        self.menu_setup()
        
        self.page.title = "Routes Example..."
        self.page.on_route_change = self.route_change
        self.page.on_view_pop = self.view_pop
        self.page.go(self.page.route)
    
    def close_drawer(self, e, route):
        self.drawer.open = False
        self.page.update()
        self.page.go(route)

    def menu_setup(self):
        self.drawer = ft.NavigationDrawer(
            controls=[
                ft.FilledTonalButton(
                    "Visit Store"
                    , icon=ft.icons.STORE
                     , on_click=lambda e: self.close_drawer(e, "/store")
                )
#                 , ft.ElevatedButton(
#                     "Visit Store"
#                     , icon=ft.icons.STORE
#                     , on_click=lambda _: self.page.go("/store")
#                 )
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
    
    def nav_bar_setup(self):
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

    def nav_rail_setup(self):
        self.nav_rail = ft.NavigationRail(
            selected_index=0,
            label_type=ft.NavigationRailLabelType.ALL,
            min_width=100,
            min_extended_width=400,
            leading=ft.FloatingActionButton(icon=ft.icons.CREATE, text="Add"),
            group_alignment=-0.9,
            destinations=[
                ft.NavigationRailDestination(
                    icon=ft.icons.FAVORITE_BORDER, selected_icon=ft.icons.FAVORITE, label="First"
                ),
                ft.NavigationRailDestination(
                    icon_content=ft.Icon(ft.icons.BOOKMARK_BORDER),
                    selected_icon_content=ft.Icon(ft.icons.BOOKMARK),
                    label="Second",
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.SETTINGS_OUTLINED,
                    selected_icon_content=ft.Icon(ft.icons.SETTINGS),
                    label_content=ft.Text("Settings"),
                ),
            ],
            on_change=lambda e: print("Selected destination:", e.control.selected_index),
        )

    def build(self):
#         self.build_appbar()
        
        self.page.update()
        
    def route_change(self, route):
        self.page.views.clear()
        self.page.views.append(
            ft.View(
                "/"
                , [
                    #self.nav_rail
                    ft.VerticalDivider(width=1)
                    , ft.Column([ ft.Text("Body!!!")], alignment=ft.MainAxisAlignment.START, expand=True)
                    , ft.ElevatedButton(
                        "Visit Store"
                        , on_click=lambda _: self.page.go("/store")
                    )
                ]
                , appbar = ft.AppBar(
                    title=ft.Text("Flet app 2")
                    , bgcolor=ft.colors.SURFACE_VARIANT
#                     , actions=[
#                         ft.IconButton(ft.icons.WB_SUNNY_OUTLINED)
#                         , ft.IconButton(ft.icons.FILTER_3)
#                         , ft.PopupMenuButton(
#                             items=[
#                                 ft.PopupMenuItem(text="Item 1")
#                                 , ft.PopupMenuItem()  # divider
#                                 , ft.PopupMenuItem(
#                                     text="Checked item"
#                                     , checked=False
#                                 )
#                             ]
#                         )
#                         , ft.IconButton(icon=ft.icons.SEARCH, icon_color=ft.colors.WHITE)
#                         , ft.IconButton(
#                             icon=ft.icons.FAVORITE, icon_color=ft.colors.WHITE
#                         )
#                     ]
                )
                , drawer = self.drawer
                , navigation_bar = self.navigation_bar
            )
        )
        if self.page.route == "/store":
            self.page.views.append(
                ft.View(
                    "/store"
                    , [
                        ft.AppBar(title=ft.Text("Store"), bgcolor=ft.colors.SURFACE_VARIANT)
                        , ft.ElevatedButton("Go Home", on_click=lambda _: self.page.go("/"))
                    ]
                )
            )
        self.page.update()
        
    def view_pop(self, view):
        self.page.views.pop()
        top_view = self.page.views[-1]
        self.page.go(top_view.route)
        
#     def build_appbar(self):
#         self.appbar_items = [
#             ft.PopupMenuItem(text="Login")
#             , ft.PopupMenuItem()  # divider
#             , ft.PopupMenuItem(text="Settings")
#         ]
        
#         self.appbar = ft.AppBar(
#             leading = ft.Icon(
#                 ft.icons.GRID_GOLDENRATIO_ROUNDED
#             )
#             , leading_width = 100
#             , title = ft.Text(
#                 "Trolli"
#                 , size=32
#                 , text_align="start"
#             )
#             , center_title = False
#             , toolbar_height = 75
#             , bgcolor = ft.colors.LIGHT_BLUE_ACCENT_700
#             , actions = [
#                 ft.Container(
#                     content = ft.PopupMenuButton(
#                         items = self.appbar_items
#                     )
#                     , margin = ft.margin.only(left=50, right=25)
#                 )
#             ]
#         )
        
#         self.page.appbar = self.appbar
        
def main(page: ft.Page):
    # await asyncio.sleep(1)
    app = Teste(page)
    
ft.app(
    target=main
#     , view=ft.AppView.WEB_BROWSER
)