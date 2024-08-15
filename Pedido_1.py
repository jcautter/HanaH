import flet as ft

def main(page):
    page.title = "Detalhes do Pedido"

    def show_item_details(item):
        counter = ft.Text(value="1", text_align=ft.TextAlign.CENTER)

        def add_quantity(e):
            counter.value = str(int(counter.value) + 1)
            counter.update()

        def reduce_quantity(e):
            if int(counter.value) > 1:
                counter.value = str(int(counter.value) - 1)
                counter.update()

        item_details = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Image(src=item["image"], fit=ft.ImageFit.COVER, height=250),
                    ft.Text(item["name"], style="headlineMedium", text_align=ft.TextAlign.CENTER),
                    ft.Text(item["description"], text_align=ft.TextAlign.CENTER),
                    ft.Row(
                        controls=[
                            ft.Row(
                                controls=[
                                    ft.IconButton(ft.icons.REMOVE, on_click=reduce_quantity),
                                    counter,
                                    ft.IconButton(ft.icons.ADD, on_click=add_quantity),
                                ],
                                alignment=ft.MainAxisAlignment.START,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                            ft.ElevatedButton("Confirmar Pedido", on_click=lambda e: print("Pedido Confirmado")),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    )
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                expand=True,
                spacing=20
            ),
            padding=20,
            border_radius=ft.BorderRadius(15, 15, 15, 15),
            bgcolor=ft.colors.GREY_500,
            expand=True,
        )

        page.controls.clear()
        page.add(item_details)
        page.update()

    item_example = {
        "image": "img/Principal.jpg",
        "name": "Filé Mignon",
        "description": "Acompanhado com arroz e batata frita",
    }

    show_item_details(item_example)

ft.app(target=main)