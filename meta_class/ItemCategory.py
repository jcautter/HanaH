import flet as ft

class ItemCategory(ft.Column):
    def __init__(self, title, items,):
        super().__init__(
            [
                ft.Text(title, style="headlineMedium"),
                ft.Column(items, spacing=10)
            ],
            spacing=10
        )
    