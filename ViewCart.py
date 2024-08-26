import flet as ft
from core.CoreClientSearch import CoreClientSearch

def main(page: ft.Page):
    page.title = "Carrinho de Compras com Pesquisa"

    search = CoreClientSearch(page)
    
    cart_items = [
        {
            'name': 'Item 1',
            'quantity': 2,
            'price': 10.00
        },
        {
            'name': 'Item 2',
            'quantity': 1,
            'price': 20.00
        }
    ]

    def update_total():
        total = sum(item['quantity'] * item['price'] for item in cart_items)
        total_text.value = f"Total: R$ {total:.2f}"
        total_button.text = f"Valor Total: R$ {total:.2f}"
        page.update()

    def update_quantity(item, delta, item_card, card):
        item['quantity'] = max(0, item['quantity'] + delta)
        item_card["quantity_text"].value = str(item['quantity'])
        item_card["total_text"].value = f"Total: R$ {item['price'] * item['quantity']:.2f}"
        if item['quantity'] == 0:
            card.visible = False
        update_total()
        page.update()

    def zero_out_item(item, item_card, card):
        item['quantity'] = 0
        item_card["quantity_text"].value = str(item['quantity'])
        item_card["total_text"].value = f"Total: R$ {item['price'] * item['quantity']:.2f}"
        card.visible = False
        update_total()
        page.update()

    def create_item_card(item):
        item_name = item['name']
        price = item['price']
        quantity = item['quantity']
        
        item_card = {
            "quantity": quantity,
            "price": price,
            "total_text": ft.Text(f"Total: R$ {price * quantity:.2f}"),
            "quantity_text": ft.Text(str(quantity))
        }
        
        card = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Column(
                        controls=[
                            ft.Text(item_name, weight="bold"),
                            item_card["total_text"],
                        ],
                        expand=True
                    ),
                    ft.IconButton(
                        icon=ft.icons.REMOVE,
                        on_click=lambda e: update_quantity(item, -1, item_card, card)
                    ),
                    item_card["quantity_text"],
                    ft.IconButton(
                        icon=ft.icons.ADD,
                        on_click=lambda e: update_quantity(item, 1, item_card, card)
                    ),
                    ft.IconButton(
                        icon=ft.icons.DELETE,
                        icon_color=ft.colors.RED,
                        on_click=lambda e: zero_out_item(item, item_card, card)
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
            padding=10,
            margin=5,
            bgcolor=ft.colors.GREY_800,
            border_radius=8,
        )
        
        return card, item_card

    total_text = ft.Text(f"Total: R$ {sum(item['quantity'] * item['price'] for item in cart_items):.2f}", weight="bold")

    cards = [create_item_card(item) for item in cart_items]

    total_button = ft.OutlinedButton(
        text=f"Valor Total: R$ {sum(item['quantity'] * item['price'] for item in cart_items):.2f}",
        width=200,
    )
    
    page.add(
        ft.Column(
            controls=[
                ft.Column(
                    controls=[card for card, _ in cards],
                    spacing=10
                ),
                search,
                total_text
            ],
            spacing=10,
            expand=True
        ),
        ft.Row(
            controls=[
                total_button,
                ft.Container(
                    content=ft.ElevatedButton(
                        text="Enviar Pedido a Cozinha", 
                        icon="send", 
                        color=ft.colors.GREEN_500
                    ),
                    alignment=ft.alignment.bottom_right,
                    expand=True
                )
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )
    )

ft.app(target=main)


