import flet as ft

from core.Core import Core
from core.CoreClientTile import CoreClientTile

from data_model.DataModelClients import DataModelClients

class CoreClientSearch(Core, ft.Container):
    def __init__(self, page):
        self._props = {
            'clients': DataModelClients()._get('list')
        }
        Core.__init__(self, page)
        ft.Container.__init__(self)

        self._build_list_item()

        self._build_search_field()
        self._build_list_view()

        self.content = ft.Column(
            [
                self._search_field
                , self._list_view
            ]
        )
    
    def _build_list_item(self):
        self._list_items = {
            '{number} - {name}'.format(
                    number = client._get('associate_number')
                    , name = client._get('name')
            ): CoreClientTile(
                self.page___
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
            label="{search}:".format(search=self.TERMS.SEARCH[self._get_lang()])
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
        self.page___.update()

    def _build_list_view(self):
        self._list_view = ft.ListView(
            expand=1
            , spacing=10
            , padding=20
        )
