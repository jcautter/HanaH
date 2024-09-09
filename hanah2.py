import flet as ft

from view.ViewStore import ViewStore

def main(page: ft.Page):
    page.on_route_change = route_change
    page.views.append(ViewStore(page))
    page.go('/')

def route_change(route):
    search_route = list(filter(lambda r: r.route==route.route, route.page.views))
    if not search_route:
        route.page.views.append(ViewStore(page))
    else:
        route.page.views.remove(search_route[0])
        route.page.views.append(search_route[0])
    route.page.go(route.route)    
    route.page.update()

ft.app(target = main)