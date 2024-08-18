import flet as ft
import ItemCardapio

class Cardapio(ft.Column):
    def __init__(self):
        super().__init__(
            expand=True
            , spacing=10
            , scroll=ft.ScrollMode.AUTO
        )
        self._titles =[]
    
    def _check_title(self, title):
        while title in self._titles:
            title += 'x'
        return title

    def _add_title(self, title:str):
        title = self._check_title(title)
        self._titles.append(title)
        self.controls.append(
            ft.Text(
                title
                , style="headlineMedium"
                , key=title
            )
        )

    def _add_item(self, item:ItemCardapio):
        self.controls.append(item)