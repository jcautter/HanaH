import flet as ft

def main(page: ft.Page):
    page.title = "Formulário de Exemplo"

    text_field = ft.TextField(
        label="id:",
        hint_text="id",
        width=300
    )

    number_field = ft.TextField(
        label="Values:",
        hint_text="Values",
        width=300,
        keyboard_type=ft.KeyboardType.NUMBER
    )

    def close_dialog(e):
        page.dialog.open = False
        page.update()

    submit_button = ft.ElevatedButton(
        text="Enviar",
        on_click=lambda e: submit_form()
    )

    def submit_form():
        id = text_field.value
        values = number_field.value
        page.dialog = ft.AlertDialog(
            title=ft.Text("Formulário Enviado"),
            content=ft.Text(f"id: {id}\nValues: {values}"),
            actions=[
                ft.TextButton("OK", on_click=close_dialog)
            ]
        )
        page.dialog.open = True
        page.update()

    page.add(
        ft.Container(
            content=ft.Column(
                controls=[
                    text_field,
                    number_field,
                    submit_button
                ],
                spacing=20,
                alignment=ft.MainAxisAlignment.CENTER
            ),
            alignment=ft.alignment.center,
            expand=True
        )
    )

ft.app(target=main)
