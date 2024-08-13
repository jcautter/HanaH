import flet as ft
from ItemCardapio_ex import ItemCardapio

def main(page):
    page.title = "Card Example"
    page.add(
        ItemCardapio(
            'img/batata.png'
            , 'Batata Frita Grande'
            , 'Servida com maionese de bacon'
            , 'R$20,00'
            , 'Adicionar ao Pedido'
        )
        , ItemCardapio(
            'img/batata.png'
            , 'Batata Frita Grande 2'
            , 'Servida com maionese de bacon 2'
            , 'R$21,00'
            , 'Adicionar ao Pedido'
        )
        , ItemCardapio(
            'img/batata.png'
            , 'Batata Frita Grande 3'
            , 'Servida com maionese de bacon 3'
            , 'R$22,00'
            , 'Adicionar ao Pedido'
        ), ItemCardapio(
            'img/batata.png'
            , 'Batata Frita Grande 4'
            , 'Servida com maionese de bacon 4'
            , 'R$23,00'
            , 'Adicionar ao Pedido'
        ), ItemCardapio(
            'img/batata.png'
            , 'Batata Frita Grande 5'
            , 'Servida com maionese de bacon 5'
            , 'R$24,00'
            , 'Adicionar ao Pedido'
        )
    )
ft.app(target=main)