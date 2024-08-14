import flet as ft

class MenuCardapio(ft.Row):
    def __init__(self, cardapio):
        super().__init__(
            spacing=20
            , alignment=ft.MainAxisAlignment.CENTER
            , scroll=ft.ScrollMode.AUTO
        )
        self._btns=[]
        self._cardapio = cardapio

    def _scroll_to_title(self, key:str, duration=500):
        self._cardapio.scroll_to(key=key, duration=duration)

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