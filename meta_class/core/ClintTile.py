import flet as ft

from meta_class.data_model.DataModelClient import DataModelClient

class ClientTile(ft.ListTile):
    def __init__(self, page:ft.Page, text:str, client:DataModelClient):
        self._props = {
            'text': text
            , 'client': client
        }
        super().__init__()
        self.___page = page

        self.title=ft.Text(self._props['text'])
        self.leading=ft.Icon(ft.icons.ACCESSIBILITY)
        self.on_click=lambda e: self.on_click_tile(e, self._props['client'])

    def _get_lang(self):
        return self.___page.client_storage.get("user")['lang']
    
    def on_click_tile(self, e, client):
        print(client._get_dict())