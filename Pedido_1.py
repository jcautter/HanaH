import flet as ft
from meta_class.ItemCardapio import ItemCardapio

def main(page):
    page.title = "Detalhes do Pedido"

    def show_order_details(item: ItemCardapio):
        quantity = 1
        item_value = float(item._props['item_value'].replace("R$", "").replace(",", "."))

        quantity_text = ft.Text(value="1", style="headlineMedium")
        total_value_text = ft.Text(f"R${item_value:.2f}", style="bodyMedium")

        def update_quantity(change):
            nonlocal quantity
            quantity += change
            if quantity < 1:
                quantity = 1
            quantity_text.value = str(quantity)
            total_value_text.value = f"R${item_value * quantity:.2f}"
            page.update()

        card = ft.Container(
            content=ft.Column(
                [
                    ft.Image(
                        src=item._props['img_path'],
                        width=page.window_width,
                        height=page.window_height * 0.4, 
                        fit=ft.ImageFit.COVER,
                    ),
                    ft.Text(
                        item._props['title'],
                        style="headlineLarge",
                        text_align=ft.TextAlign.LEFT,
                    ),
                    ft.Text(
                        item._props['subtitle'],
                        style="bodyMedium",
                        text_align=ft.TextAlign.LEFT,
                    ),
                    ft.Container(expand=True),
                    ft.Row(
                        controls=[
                            ft.Row(
                                controls=[
                                    ft.IconButton(ft.icons.REMOVE, on_click=lambda _: update_quantity(-1)),
                                    quantity_text,
                                    ft.IconButton(ft.icons.ADD, on_click=lambda _: update_quantity(1)),
                                ],
                                alignment=ft.MainAxisAlignment.START,
                            ),
                            ft.Column(
                                [
                                    ft.Text("Total:", style="bodyMedium"),
                                    total_value_text
                                ],
                                alignment=ft.MainAxisAlignment.END,
                            ),
                            ft.ElevatedButton(
                                text="Confirmar Pedido",
                                on_click=lambda _: print("Pedido Confirmado!"),
                                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8)),
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                ],
                spacing=15,
                width=page.window_width * 0.9,
                expand=True,
            ),
            padding=20,
            expand=True
        )

        page.controls.clear()
        page.add(card)
        page.update()

    example_item = ItemCardapio(
        'img/Principal.jpg',
        'Filé Mignon',
        'Acompanhado com arroz e batata frita',
        'R$45,00',
        'Adicionar ao Pedido'
    )

    show_order_details(example_item)

ft.app(target=main)
