import flet as ft

def main(page):
    page.title = "Pedidos"
    
    def cancel_order(e):
        print("Pedido Cancelado")

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
                '3x Suco de Laranja',
                '1x Italiano'
            ]
        },
        {
            'garcom': 'Pedro Almeida',
            'cliente': 'Fernanda Lima',
            'itens': [
                '2x Torresmo',
                '1x Água Mineral'
            ]
        },
        {
            'garcom': 'Pedro Almeida',
            'cliente': 'Fernanda Lima',
            'itens': [
                '2x Torresmo',
                '1x Água Mineral'
            ]
        }
    ]
    
    tiles = []
    for index, pedido in enumerate(pedidos):
        tile_content = ft.Column(
            controls=[
                ft.Text(f"Garçom: {pedido['garcom']}", style="headlineSmall", color=ft.colors.BLUE_500),
                ft.Text(f"Cliente: {pedido['cliente']}", style="headlineSmall", color=ft.colors.BLUE_500),
                ft.Text("Pedido:", style="headlineSmall", color=ft.colors.BLUE_500),
                ft.Column(
                    controls=[ft.Text(item, style="bodyBig", color=ft.colors.AMBER_500) for item in pedido['itens']],
                    spacing=5
                ),
            ],
            spacing=10
        )
        
        tile = ft.Dismissible(
            content=ft.Container(
                content=tile_content,
                bgcolor=ft.colors.GREY_700,
                border_radius=8,
                padding=10,
                border=ft.Border(
                    left=ft.BorderSide(width=2, color=ft.colors.GREY),
                    top=ft.BorderSide(width=2, color=ft.colors.GREY),
                    right=ft.BorderSide(width=2, color=ft.colors.GREY),
                    bottom=ft.BorderSide(width=2, color=ft.colors.GREY)
                ),
                width=page.window_width
            ),
            on_dismiss=lambda e, idx=index: cancel_order(idx),
            background=ft.Container(
                content=ft.Text("Cancelar Pedido", color=ft.colors.WHITE, style="headlineMedium"),
                bgcolor=ft.colors.RED,
                alignment=ft.Alignment(-1, 0),
                width=120
            ),
            dismiss_direction=ft.DismissDirection.END_TO_START
        )
        
        tiles.append(tile)
    
    page.add(ft.ListView(
        controls=tiles,
        spacing=10,
        expand=True,
        width=page.window_width
    ))

ft.app(target=main)
