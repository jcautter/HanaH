import flet as ft

from core.Core import Core

from core.CoreCatalog import CoreCatalog

class CoreCatalogMenu(Core, ft.Row):
    def __init__(self, page:ft.Page, catalog:CoreCatalog):
        Core.__init__(self, page)
        ft.Row.__init__(
            self
            , spacing=20
            , alignment=ft.MainAxisAlignment.CENTER
            , scroll=ft.ScrollMode.AUTO
        )
        self._btns = []
        self._catalog = catalog
        
        self.search_bar = ft.SearchBar(
            view_elevation=4,
            divider_color=ft.colors.AMBER,
            bar_hint_text="Pesquisar itens...",
            view_hint_text="Escolha um item do cardápio...",
            on_change=self._on_search_change,
            on_submit=self._on_search_submit,
            on_tap=self._on_search_tap,
            controls=[]
        )
        
        self.controls.append(self.search_bar)
        self._original_controls = {section.key: section.controls[:] for section in catalog.controls}

    def _get_lang(self):
        return self.page___.client_storage.get("user")['lang']

    def _scroll_to_title(self, key: str, duration=500):
        self._catalog.scroll_to(key=key, duration=duration)

    def _check_btn(self, btn):
        while btn in self._btns:
            btn += 'x'
        return btn
    
    def _add_item(self, btn: str):
        btn = self._check_btn(btn)
        self._btns.append(btn)
        self.controls.append(
            ft.TextButton(btn, on_click=lambda _: self._scroll_to_title(key=btn))
        )

    def _on_search_change(self, e):
        search_term = e.data.lower()
        self._filter_items(search_term)

    def _on_search_submit(self, e):
        search_term = e.data.lower()
        self._filter_items(search_term)

    def _on_search_tap(self, e):
        print("Pesquisa iniciada")

    def _filter_items(self, search_term):
        self._catalog.controls.clear()

        if search_term.strip() == "":
            for key, controls in self._original_controls.items():
                section = ft.Column(controls=controls, key=key)
                self._catalog.controls.append(section)
        else:
            for key, controls in self._original_controls.items():
                filtered_controls = [
                    item for item in controls
                    if search_term in item._props['title'].lower()
                ]
                if filtered_controls:
                    section = ft.Column(
                        controls=filtered_controls,
                        key=key
                    )
                    self._catalog.controls.append(section)
        
        self._catalog.update()
