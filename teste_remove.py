import flet as ft

def main(page: ft.Page):
    page.title = "Carrinho de Compras com Pesquisa"
    bt = ft.TextButton(
        'Apagar'
        , on_click=lambda e: page.remove(bt)
    )
    
    page.add(
        bt
    )


ft.app(target=main)