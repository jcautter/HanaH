import flet as ft

from config.common import (Route, Language, Terms)

from meta_class.core.Order import Order

class ViewOrder(ft.View):
    def __init__(self, page):
        route = Route.ORDER
        super().__init__(route=route)
        self.___page = page
        self._buid()

    def _get_lang(self):
        return self.___page.client_storage.get("user")['lang']
    
    def _buid(self):
        self._build_controls()
        self._build_appbar()

    def _build_controls(self):
        
        pedido = Order(
            **{
                'img_path': 'img/Principal.jpg'
                , 'title': 'Filé Mignon'
                , 'description': 'Filé Mignon mal ou bem passado, acompanhado com arroz e batata frita ou purê de batata'
                , 'item_value': 49.90
                , 'quantity': 1
            }
        )
        self.controls = [
            pedido
        ]
    
    def _build_appbar(self):
        self.appbar = ft.AppBar(
            title=ft.Text("Pedido")
            , bgcolor=ft.colors.SURFACE_VARIANT
        )