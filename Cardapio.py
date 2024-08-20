import flet as ft
from meta_class.ItemCardapio import ItemCardapio

def main(page):
    page.title = "Cardapio"

    def create_category_section(title, items, key):
        return ft.Column(
            [
                ft.Text(title, style="headlineMedium", key=key),
                ft.Column(items, spacing=10)
            ],
            spacing=10,
            key=key
        )
    
    bebidas_section = create_category_section(
        "Bebidas",
        [
            ItemCardapio(
                'img/Bebida.jpg',
                'Suco de Laranja',
                'Com ou Sem açúcar',
                'a',
                'R$9,00',
                'Adicionar ao Pedido'
            ),
            ItemCardapio(
                'img/Bebida.jpg',
                'Cerveja',
                'Antarctica, Brahma, Heineken',
                'a',
                'R$12,00',
                'Adicionar ao Pedido'
            )
        ],
        key="bebidas_section"
    )
    
    entradas_section = create_category_section(
        "Entradas",
        [
            ItemCardapio(
                'img/batata.png',
                'Batata Frita Grande',
                'Servida com maionese de bacon',
                'a',
                'R$20,00',
                'Adicionar ao Pedido'
            ),
            ItemCardapio(
                'img/Entrada.jpg',
                'Torresmo',
                'Feita na hora',
                'a',
                'R$21,00',
                'Adicionar ao Pedido'
            )
        ],
        key="entradas_section"
    )
    
    principais_section = create_category_section(
        "Pratos Principais",
        [
            ItemCardapio(
                'img/Principal.jpg',
                'Filé Mignon',
                'Acompanhado com arroz e batata frita',
                'a',
                'R$45,00',
                'Adicionar ao Pedido'
            ),
            ItemCardapio(
                'img/Principal.jpg',
                'Frango à Parmegiana',
                'Acompanhado com purê de batata',
                'a',
                'R$40,00',
                'Adicionar ao Pedido'
            ),
            ItemCardapio(
                'img/Principal.jpg',
                'Filé Oswaldo Aranha',
                'Acompanhado com arroz e batata frita',
                'a',
                'R$524,00',
                'Adicionar ao Pedido'
            )
        ],
        key="principais_section"
    )
    
    sections = [bebidas_section, entradas_section, principais_section]
    
    def scroll_to_section(key: str, duration=500):
        list_view.scroll_to(key=key, duration=duration)

    menu = ft.Row(
        [
            ft.TextButton("Bebidas", on_click=lambda _: scroll_to_section(key="bebidas_section")),
            ft.TextButton("Entradas", on_click=lambda _: scroll_to_section(key="entradas_section")),
            ft.TextButton("Pratos Principais", on_click=lambda _: scroll_to_section(key="principais_section"))
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

    # Adiciona o menu e a lista de categorias à página
    page.add(ft.Column([
        menu,
        list_view
    ]))

ft.app(target=main)
