import flet as ft

from config.common import (Route, Language, Terms)

from data_model.DataModelUser import DataModelUser

from view.ViewRoot import ViewRoot
from view.ViewOrder import ViewOrder
from view.ViewStore import ViewStore
from view.ViewNovaview import ViewNovaview
from view.ViewCart import ViewCart

class Hanah:
    def __init__(self, page: ft.Page):
        self.page = page
        self.build()
        self.page_setup()
        usr = DataModelUser(login='gar1')
        usr._push_cokies(self.page)

    
    def page_setup(self):
        self.page.title = "HanaH"
        self.page.on_route_change = self.route_change
        self.page.on_view_pop = self.view_pop
        self.page.window.width=360
        self.page.window.height=640
        self.page.window.resizable = False
        self.page.go('/')

    def build(self):
        self.page.update()
    
    def route_change(self, route):
        search_route = list(filter(lambda r: r.route==route.route, route.page.views))
        if not search_route:
            # match route.route:
            #     case Route.ROOT:
            #         route.page.views.append(ViewRoot())
            #     case Route.ORDER:
            #         route.page.views.append(ViewStore())
            #     case Route.NOVAVIEW:
            #         route.page.views.append(ViewNovaview())
            if route.route == Route.ROOT:
                route.page.views.append(ViewRoot(self.page))
            elif route.route == Route.ORDER:
                route.page.views.append(ViewOrder(self.page))
            elif route.route == Route.CART:
                route.page.views.append(ViewCart(self.page))
            elif route.route == Route.STORE:
                route.page.views.append(ViewStore(self.page))
            elif route.route == Route.NOVAVIEW:
                route.page.views.append(ViewNovaview(self.page))
        else:
            route.page.views.remove(search_route[0])
            route.page.views.append(search_route[0])
        route.page.go(route.route)    
        route.page.update()
        
    def view_pop(self, view):
        if view.page.views:
            view.page.views.pop()
            if view.page.views:
                view.page.go(self.page.views[-1].route)
        
def main(page: ft.Page):
    # app = Teste(page)
    Hanah(page)
    
ft.app(
    target=main
#     , view=ft.AppView.WEB_BROWSER
)