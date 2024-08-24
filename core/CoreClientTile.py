import flet as ft

from core.Core import Core

from data_model.DataModelClient import DataModelClient

class CoreClientTile(Core, ft.ListTile):
    def __init__(self, page:ft.Page, text:str, client:DataModelClient):
        self._props = {
            'text': text
            , 'client': client
        }
        Core.__init__(self, page)
        ft.ListTile.__init__(self)

        self.title=ft.Text(self._props['text'])
        self.leading=ft.Icon(ft.icons.ACCESSIBILITY)
        self.on_click=lambda e: self._on_click_tile(e, self._props['client'])
    
    def _on_click_tile(self, e, client):
        print(client._get_dict())