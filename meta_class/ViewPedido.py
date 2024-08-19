import flet as ft

from meta_class.core.Pedido import Pedido

class ViewPedido(ft.View):
    def __init__(self):
        route = '/pedido'
        super().__init__(route=route)
        self._buid()

    def _buid(self):
        self._build_controls()
        self._build_appbar()

    def _build_controls(self):
        
        pedido = Pedido(
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
            title=ft.Text("Confirmar")
            , bgcolor=ft.colors.SURFACE_VARIANT
        )