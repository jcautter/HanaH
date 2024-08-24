import flet as ft

from meta_class.core.ClientSearch import ClientSearch

def main(page: ft.Page):
    page.title = "Autocomplete search names"
    page.add(
        ClientSearch(page)
    )
    from datetime import datetime
    print(type(datetime.now().isoformat(timespec='minutes')))

ft.app(
    target=main
    # , view=ft.WEB_BROWSER
    # , port=8080
)