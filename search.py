import flet as ft

from meta_class.data_model.DataModelClients import DataModelClients

NAMES = [
    'Adam',
    'William',
    'Emma',
    'Alexander',
    'Julia',
    'Elias',
    'Hugo',
    'Alice',
    'Emil',
    'Anton',
    'Ebba',
    'Elin',
    'Oliver',
    'Axel',
    'Maja',
    'Ella',
    'Alva',
    'Liam',
    'Albin',
    'Elsa',
    'Erik',
    'Ida',
    'Oscar',
    'Wilma'
]

dados = DataModelClients()

for client in dados._get('list'):
    NAMES.append('{number} - {name}'.format(
        number = client._get('associate_number')
        , name = client._get('name')
    ))

def printer(e, client):
    print('Yellow!')
    print(client._get_dict())


class Client(ft.ListTile):
    def __init__(self, text, client):
        super().__init__()
        self.title=ft.Text(text)
        self.leading=ft.Icon(ft.icons.ACCESSIBILITY)
        self.on_click=lambda e: printer(e, client)

def main(page: ft.Page):
    page.title = "Autocomplete search names"

    def textbox_changed(string):
        str_lower = string.control.value.lower()
        # list_view.controls = [
        #     list_items.get(n) for n in NAMES if str_lower in n.lower()
        # ] if str_lower else []
        list_view.controls = [
            list_items.get('{number} - {name}'.format(
                number = client._get('associate_number')
                , name = client._get('name')
            )) for client in dados._get('list') if str_lower in '{number} - {name}'.format(
                number = client._get('associate_number')
                , name = client._get('name')
            ).lower()
        ] if str_lower else []
        page.update()

    # list_items = {
    #     name: ft.ListTile(
    #         title=ft.Text(name),
    #         leading=ft.Icon(ft.icons.ACCESSIBILITY),
    #         on_click=printer
    #     )
    #     for name in NAMES
    # }

    list_items = {
        '{number} - {name}'.format(
                number = client._get('associate_number')
                , name = client._get('name')
        ): Client(
            '{number} - {name}'.format(
                    number = client._get('associate_number')
                    , name = client._get('name')
            )
            , client
        )
        for client in dados._get('list')
    }

    text_field = ft.TextField(label="Search name:", on_change=textbox_changed)
    list_view = ft.ListView(expand=1, spacing=10, padding=20)

    page.add(text_field, list_view)


ft.app(
    target=main
    # , view=ft.WEB_BROWSER
    # , port=8080
)