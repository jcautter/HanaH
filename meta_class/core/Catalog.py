import flet as ft
from meta_class.core.ProductCatalog import ProductCatalog

class Catalog(ft.Column):
    def __init__(self, page):
        super().__init__(
            expand=True
            , spacing=10 
            , scroll=ft.ScrollMode.AUTO
        )
        self._titles = []
        self.___page = page
    
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

    def _add_item(self, item:ProductCatalog):
        self.controls.append(item)