import flet as ft
from meta_class.Pedido import Pedido



def main(page:ft.Page):
    page.title = "Detalhes do Pedido"
    page.window_width=360
    page.window_height=640
    page.window_resizable = False

    pedido = Pedido(
         **{
            'img_path': 'img/Principal.jpg'
            , 'title': 'Filé Mignon'
            , 'description': 'Filé Mignon mal ou bem passado, acompanhado com arroz e batata frita ou purê de batata'
            , 'item_value': 49.90
            , 'quantity': 1
         }
    )
    page.add(pedido)

ft.app(target=main)