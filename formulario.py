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

    toggle_switch = ft.Switch(
        label="Ativar Opção",
        value=False,
    )

    teams = ["Flamengo", "Vasco", "Botafogo", "Fluminense", "São Paulo"]
    team_dropdown = ft.Dropdown(
        label="Escolha um time",
        options=[ft.dropdown.Option(text=team) for team in teams],
        width=300
    )

    checkbox_colors = ["red", "green", "blue", "yellow", "purple"]
    current_color_index = 0

    checkbox_container = ft.Container(
        width=20,
        height=20,
        bgcolor=checkbox_colors[current_color_index],
        border_radius=4,
        on_click=lambda e: toggle_color(),
    )

    def toggle_color():
        nonlocal current_color_index
        current_color_index = (current_color_index + 1) % len(checkbox_colors)
        checkbox_container.bgcolor = checkbox_colors[current_color_index]
        page.update()

    submit_button = ft.ElevatedButton(
        text="Enviar",
        on_click=lambda e: submit_form()
    )

    def close_dialog(e):
        page.dialog.open = False
        page.update()

    def submit_form():
        id_value = text_field.value
        number_value = number_field.value
        selected_team = team_dropdown.value
        page.dialog = ft.AlertDialog(
            title=ft.Text("Formulário Enviado"),
            content=ft.Text(f"id: {id_value}\nValues: {number_value}\nTime Selecionado: {selected_team}"),
            actions=[
                ft.TextButton("OK", on_click=close_dialog)
            ]
        )
        page.dialog.open = True
        page.update()

    center_container = ft.Container(
        content=ft.Column(
            controls=[
                toggle_switch,
                text_field,
                number_field,
                team_dropdown,
                checkbox_container,
                submit_button,
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        alignment=ft.Alignment(0, 0),
        expand=True
    )

    page.add(center_container)

ft.app(target=main)
