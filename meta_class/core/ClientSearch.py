import flet as ft

from config.common import (Route, Language, Terms)

from meta_class.data_model.DataModelClients import DataModelClients

from meta_class.core.ClintTile import ClientTile

class ClientSearch(ft.Container):
    def __init__(self, page):
        self._props = {
            'clients': DataModelClients()._get('list')
        }
        super().__init__()
        self.___page = page

        self._build_list_item()

        self._build_search_field()
        self._build_list_view()

        self.content = ft.Column(
            [
                self._search_field
                , self._list_view
            ]
        )

    def _get_lang(self):
        return self.___page.client_storage.get("user")['lang']
    
    def _build_list_item(self):
        self._list_items = {
            '{number} - {name}'.format(
                    number = client._get('associate_number')
                    , name = client._get('name')
            ): ClientTile(
                self.___page
                , '{number} - {name}'.format(
                        number = client._get('associate_number')
                        , name = client._get('name')
                )
                , client
            )
            for client in self._props['clients']
        }

    def _build_search_field(self):
        self._search_field = ft.TextField(
            label="{search}:".format(search=Terms.SEARCH[self._get_lang()])
            , on_change=self._textbox_changed
        )

    def _textbox_changed(self, string):
        str_lower = string.control.value.lower()
        self._list_view.controls = [
            self._list_items.get('{number} - {name}'.format(
                number = client._get('associate_number')
                , name = client._get('name')
            )) for client in self._props['clients'] if str_lower in '{number} - {name}'.format(
                number = client._get('associate_number')
                , name = client._get('name')
            ).lower()
        ] if str_lower else []
        self.___page.update()

    def _build_list_view(self):
        self._list_view = ft.ListView(
            expand=1
            , spacing=10
            , padding=20
        )
