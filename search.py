import flet as ft

from core.CoreClientSearch import CoreClientSearch

def main(page: ft.Page):
    page.title = "Autocomplete search names"
    page.add(
        CoreClientSearch(page)
    )

ft.app(
    target=main
    # , view=ft.WEB_BROWSER
    # , port=8080
)