import flet as ft
from meta_class.ItemCardapio import ItemCardapio
from meta_class.ItemCategory import ItemCategory

def main(page):
    page.title = "Cardapio"

    bebidas_item = [
        ItemCardapio(
            'img/Bebida.jpg',
            'Suco de Laranja',
            'Com ou Sem açúcar',
            'R$9,00',
            'Adicionar ao Pedido'
        ),
        ItemCardapio(
            'img/Bebida.jpg',
            'Cerveja',
            'Antarctica, Brahma, Heineken',
            'R$12,00',
            'Adicionar ao Pedido'
        )
    ]

    entradas_item = [
        ItemCardapio(
            'img/batata.png',
            'Batata Frita Grande',
            'Servida com maionese de bacon',
            'R$20,00',
            'Adicionar ao Pedido'
        ),
        ItemCardapio(
            'img/Entrada.jpg',
            'Torresmo',
            'Feita na hora',
            'R$21,00',
            'Adicionar ao Pedido'
        )
    ]

    principal_item = [
        ItemCardapio(
            'img/Principal.jpg',
            'Filé Mignon',
            'Acompanhado com arroz e batata frita',
            'R$45,00',
            'Adicionar ao Pedido'
        ),
        ItemCardapio(
            'img/Principal.jpg',
            'Frango à Parmegiana',
            'Acompanhado com purê de batata',
            'R$40,00',
            'Adicionar ao Pedido'
        ),
        ItemCardapio(
            'img/Principal.jpg',
            'Filé Oswaldo Aranha',
            'Acompanhado com arroz e batata frita',
            'R$524,00',
            'Adicionar ao Pedido'
        )
    ]
    
    bebidas_section = ItemCategory("Bebidas", bebidas_item)
    entradas_section = ItemCategory("Entradas", entradas_item)
    principal_section = ItemCategory("Pratos Principais", principal_item)
    sections = [bebidas_section, entradas_section, principal_section]

    def update_visibility(selection):
        for section in sections:
            section.visible = (selection == "all") or (section.controls[0].value.lower() == selection.lower())
        page.update()

    menu = ft.Row(
        [
            ft.TextButton("Tudo", on_click=lambda _: update_visibility('all')),
            ft.TextButton("Bebidas", on_click=lambda _: update_visibility('bebidas')),
            ft.TextButton("Entradas", on_click=lambda _: update_visibility('entradas')),
            ft.TextButton("Pratos Principais", on_click=lambda _: update_visibility('pratos principais')),
        ],
        spacing=20,
        alignment=ft.MainAxisAlignment.CENTER
    )
    
    page.add(menu,*sections)
    update_visibility('all')

ft.app(target=main)
