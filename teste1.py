import flet as ft
from meta_class.ViewRoot import ViewRoot
from meta_class.ViewStore import ViewStore
from meta_class.ViewNovaview import ViewNovaview

class Teste:
    def __init__(self, page: ft.Page):
        self.page = page
        self.build()
        self.page_setup()

    
    def page_setup(self):
        self.page.title = "Routes Example..."
        self.page.on_route_change = self.route_change
        self.page.on_view_pop = self.view_pop
        self.page.go('/')

    def build(self):        
        self.page.update()
    
    def route_change(self, route):
        # self.page.views.clear()
        search_route = list(filter(lambda r: r.route==route.route, route.page.views))
        if not search_route:
            # match route.route:
            #     case '/':
            #         route.page.views.append(ViewRoot())
            #     case "/store":
            #         route.page.views.append(ViewStore())
            #     case "/novaview":
            #         route.page.views.append(ViewNovaview())
            if route.route == '/':
                route.page.views.append(ViewRoot())
            elif route.route == "/store":
                route.page.views.append(ViewStore())
            elif route.route == "/novaview":
                route.page.views.append(ViewNovaview())
        else:
            route.page.views.remove(search_route[0])
            route.page.views.append(search_route[0])
        route.page.go(route.route)    
        route.page.update()
        
    def view_pop(self, view):
        # print(view)
        # print(dir(view))
        if view.page.views:
            view.page.views.pop()
            if view.page.views:
                view.page.go(self.page.views[-1].route)
        
def main(page: ft.Page):
    # app = Teste(page)
    Teste(page)
    
ft.app(
    target=main
#     , view=ft.AppView.WEB_BROWSER
)