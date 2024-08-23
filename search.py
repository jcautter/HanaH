import flet as ft

from meta_class.core.ClientSearch import ClientSearch

def main(page: ft.Page):
    page.title = "Autocomplete search names"
    page.add(ClientSearch(page))

ft.app(
    target=main
    # , view=ft.WEB_BROWSER
    # , port=8080
)