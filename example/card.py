import flet as ft

def main(page):
    page.title = "Card Example"
    page.add(
        ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Row(
                            [
                                ft.Image(
                                    src=f"img/batata.png",
                                    width=150,
                                    height=150,
                                    fit=ft.ImageFit.FILL
                                )
                                , ft.Column(
                                    [
                                        ft.ListTile(
                                            title=ft.Text("Batata Frita Grande"),
                                            subtitle=ft.Text(
                                                "Servida com maionese de bacon"
                                            ),
                                        )
                                        ,ft.Row(
                                            [
                                                ft.TextButton("Adicionar ao Pedido"),
                                                ft.Text("Valor=R$20")
                                            ]
                                        )
                                        
                                    ]
                                )
                            ]

                        )  
                    ]
                )
                #, width=300
                , padding=5
            )
        )
    )

ft.app(target=main)