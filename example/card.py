import flet as ft

def main(page):
    page.title = "Card Example"
    page.add(
        ft.Card(
            content=ft.Container(
                content=ft.Row(
                    [
                        ft.Image(
                            src=f"img/batata.png",
                            width=150,
                            height=150,
                            fit=ft.ImageFit.FILL
                        ),
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.ListTile(
                                        title=ft.Text("Batata Frita Grande"),
                                        subtitle=ft.Text(
                                            "Servida com maionese de bacon"
                                        ),
                                    ),
                                    ft.Row(
                                        [
                                            ft.Container(
                                                content=ft.Text("R$20,00", color=ft.colors.BLUE_500),
                                                alignment=ft.alignment.center_left
                                            ),
                                            ft.Container(
                                                content=ft.TextButton("Adicionar ao Pedido"),
                                                alignment=ft.alignment.center_right
                                            )
                                        ]
                                        , alignment = ft.MainAxisAlignment.SPACE_BETWEEN
                                    )
                                ],
                                alignment=ft.MainAxisAlignment.START,
                                spacing=5
                            ),
                            expand=True
                        )
                    ],
                    alignment=ft.MainAxisAlignment.START
                ),
                padding=5
            )
        )
    )

ft.app(target=main)
