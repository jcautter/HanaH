import flet as ft

from config.common import (Route, Language, Terms)

class Core:
    ROUTE = Route
    LANGUAGE = Language
    TERMS = Terms

    def __init__(self, page:ft.Page):
        self.page___ = page

    def _get_lang(self):
        return self.page___.client_storage.get("user")['lang']
    
    def _view_pop(self, view:ft.View=None):
        if not view:
            view = self.page___.views[-1]
        if view.page.views:
            view.page.views.pop()
            if view.page.views:
                view.page.go(self.page.views[-1].route)