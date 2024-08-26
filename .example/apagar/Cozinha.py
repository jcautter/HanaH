import flet as ft

def main(page):
    page.title = "Cozinha - Pedidos"
    page.scroll = ft.ScrollMode.AUTO

    pedidos = [
        {
            'garcom': 'João Silva',
            'cliente': 'Maria Oliveira',
            'itens': [
                '1x Batata Frita Grande',
                '2x Suco de Laranja',
                '2x Filé Mignon'
            ]
        },
        {
            'garcom': 'Ana Souza',
            'cliente': 'Carlos Santos',
            'itens': [
                '3x Hambúrguer',
                '1x Salada Caesar'
            ]
        },
                {
            'garcom': 'João Silva',
            'cliente': 'Maria Oliveira',
            'itens': [
                '1x Batata Frita Grande',
                '2x Suco de Laranja',
                '2x Filé Mignon'
            ]
        },
        {
            'garcom': 'Ana Souza',
            'cliente': 'Carlos Santos',
            'itens': [
                '3x Hambúrguer',
                '1x Salada Caesar'
            ]
        },
                {
            'garcom': 'João Silva',
            'cliente': 'Maria Oliveira',
            'itens': [
                '1x Batata Frita Grande',
                '2x Suco de Laranja',
                '2x Filé Mignon'
            ]
        },
        {
            'garcom': 'Ana Souza',
            'cliente': 'Carlos Santos',
            'itens': [
                '3x Hambúrguer',
                '1x Salada Caesar'
            ]
        },
                {
            'garcom': 'João Silva',
            'cliente': 'Maria Oliveira',
            'itens': [
                '1x Batata Frita Grande',
                '2x Suco de Laranja',
                '2x Filé Mignon'
            ]
        },
        {
            'garcom': 'Ana Souza',
            'cliente': 'Carlos Santos',
            'itens': [
                '3x Hambúrguer',
                '1x Salada Caesar'
            ]
        },
                {
            'garcom': 'João Silva',
            'cliente': 'Maria Oliveira',
            'itens': [
                '1x Batata Frita Grande',
                '2x Suco de Laranja',
                '2x Filé Mignon'
            ]
        },
        {
            'garcom': 'Ana Souza',
            'cliente': 'Carlos Santos',
            'itens': [
                '3x Hambúrguer',
                '1x Salada Caesar'
            ]
        },
                {
            'garcom': 'João Silva',
            'cliente': 'Maria Oliveira',
            'itens': [
                '1x Batata Frita Grande',
                '2x Suco de Laranja',
                '2x Filé Mignon'
            ]
        },
        {
            'garcom': 'Ana Souza',
            'cliente': 'Carlos Santos',
            'itens': [
                '3x Hambúrguer',
                '1x Salada Caesar'
            ]
        }
    ]

    def pedido_pronto(e):
        e.control.disabled = True
        e.control.text = "Pronto!"
        e.control.icon = ft.icons.CHECK_CIRCLE_OUTLINE
        e.control.update()

    def create_order_card(order):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(f"Garçom: {order['garcom']}", weight="bold", color=ft.colors.BLUE_GREY_500),
                    ft.Text(f"Cliente: {order['cliente']}", weight="bold", color=ft.colors.BLUE_GREY_500),
                    ft.Text("Itens:", weight="bold", color=ft.colors.BLUE_GREY_500),
                    ft.Column(
                        controls=[ft.Text(item) for item in order['itens']],
                        spacing=2
                    ),
                    ft.Container(
                        content=ft.ElevatedButton(
                            text="Pedido Pronto",
                            icon=ft.icons.CHECK,
                            on_click=pedido_pronto,
                            bgcolor=ft.colors.GREEN_500,
                            color=ft.colors.WHITE
                        ),
                        alignment=ft.alignment.bottom_center
                    )
                ],
                spacing=5,
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN 
            ),
            padding=10,
            width=200,
            height=250,
            bgcolor=ft.colors.GREY_500,
            border_radius=8,
        )

    grid = ft.Row(
        controls=[
            create_order_card(order)
            for order in pedidos
        ],
        wrap=True,
        alignment=ft.MainAxisAlignment.START,
        spacing=10
    )

    page.add(grid)

ft.app(target=main)

