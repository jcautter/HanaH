import flet as ft

from config.common import (Route, Language, Terms)

class MenuCatalog(ft.Row):
    def __init__(self, page, catalog):
        super().__init__(
            spacing=20
            , alignment=ft.MainAxisAlignment.CENTER
            , scroll=ft.ScrollMode.AUTO
        )
        self.___page = page
        self._btns=[]
        self._catalog = catalog

    def _get_lang(self):
        return self.___page.client_storage.get("user")['lang']

    def _scroll_to_title(self, key:str, duration=500):
        self._catalog.scroll_to(key=key, duration=duration)

    def _check_btn(self, btn):
        while btn in self._btns:
            btn += 'x'
        return btn
    
    def _add_item(self, btn:str):
        btn = self._check_btn(btn)
        self._btns.append(btn)
        self.controls.append(
            ft.TextButton(btn, on_click=lambda _: self._scroll_to_title(key=btn))
        )