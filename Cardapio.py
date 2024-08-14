import flet as ft
from meta_class.ItemCardapio import ItemCardapio

def main(page):
    page.title = "Cardapio"

    def create_category_section(title, items):
        return ft.Column(
            [
                ft.Text(title, style="headlineMedium"),
                ft.Column(items, spacing=10)
            ],
            spacing=10
        )
    
    bebidas_section = create_category_section(
        "Bebidas",
        [
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
    )
    
    entradas_section = create_category_section(
        "Entradas",
        [
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
    )
    
    principais_section = create_category_section(
        "Pratos Principais",
        [
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
    )
    
    sections = [bebidas_section, entradas_section, principais_section]
    
    def scroll_to_section(key:str, duration=500):
        list_view.scroll_to(key=key, duration=duration)

    menu = ft.Row(
        [
            ft.TextButton("Bebidas", on_click=lambda _: scroll_to_section(key="0")),
            ft.TextButton("Entradas", on_click=lambda _: scroll_to_section(key="2")),
            ft.TextButton("Pratos Principais", on_click=lambda _: scroll_to_section(key="4")),
            ft.TextButton("Pratos Principais2", on_click=None),
            ft.TextButton("Pratos Principais3", on_click=None),
            ft.TextButton("Pratos Principais4", on_click=None),
            ft.TextButton("Pratos Principais5", on_click=None),
            ft.TextButton("Pratos Principais6", on_click=None),
            ft.TextButton("Pratos Principais7", on_click=None),
            ft.TextButton("Pratos Principais8", on_click=None),
            ft.TextButton("Pratos Principais9", on_click=None),
            ft.TextButton("Pratos Principais10", on_click=None),
            ft.TextButton("Pratos Principais11", on_click=None),
            ft.TextButton("Pratos Principais12", on_click=None),
            ft.TextButton("Pratos Principais13", on_click=None),
        ],
        spacing=20,
        alignment=ft.MainAxisAlignment.CENTER,
        scroll=ft.ScrollMode.AUTO,
    )
    
    list_view = ft.ListView(
        expand=True,
        spacing=10,
        padding=10,
        controls=sections,
    )
    
    page.add(menu, list_view)

ft.app(target=main)
