import flet as ft

from core.Core import Core

from core.CoreCatalogProduct import CoreCatalogProduct

class CoreCatalog(Core, ft.Column):
    def __init__(self, page:ft.Page):
        Core.__init__(self, page)
        ft.Column.__init__(
            self
            , expand=True
            , spacing=10 
            , scroll=ft.ScrollMode.AUTO
        )
        self._titles = []
    
    def _check_title(self, title:str):
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

    def _add_item(self, item:CoreCatalogProduct):
        self.controls.append(item)