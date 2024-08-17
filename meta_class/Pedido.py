import flet as ft

class Pedido(ft.Container):

    def __init__(self, img_path:str, title:str, description:str, item_value:float, quantity:int=1):
        super().__init__()
        self._props = {
            'img_path': img_path
            , 'title': title
            , 'description': description
            , 'item_value': item_value
            , 'quantity': quantity
        }
        self._build()
    
    def _build(self):
        self._build_cover()
        self._build_title()
        self._build_description()
        self._bulid_bottom()

        self.content = ft.Column(
            [
                 self._cover
                 , self._title
                 , self._description
                #  , ft.Container(expand=True)
                 , self._bottom
            ]
        )

    def _go_back(self, e):
            print("Voltar")
            print(e.page.title)
            # e.page.views.pop()
            # e.page.go(e.page.views[-1].route)

    def _update_quantity(self, e, change):
            if self._props['quantity'] + change < 1:
                self._props['quantity'] = 1
            else:
                self._props['quantity'] += change
            
            self._quantity.value = str(self._props['quantity'])
            self._total.value = f"R${self._props['item_value'] * self._props['quantity']:.2f}"
            e.page.update()

    def _build_cover(self):
        self._cover = ft.Container(
            bgcolor=ft.colors.BLACK
            , content=ft.Stack(
                alignment=ft.Alignment(0, -1)
                , controls=[
                    ft.Image(
                        src=self._props['img_path']
                        , height=200
                        , fit=ft.ImageFit.COVER
                        , 
                    ),
                    ft.Container(
                        content=ft.IconButton(
                            ft.icons.CLOSE 
                            , on_click=self._go_back 
                            , icon_size=30
                            , style=ft.ButtonStyle(shape=ft.CircleBorder())
                            , bgcolor=ft.colors.WHITE                            
                        ),
                        alignment=ft.Alignment(1,0),
                        margin=10
                    ),
                ]
            )
        )

    def _build_title(self):
        self._title = ft.Text(
            self._props['title'],
            style="headlineLarge",
            text_align=ft.TextAlign.LEFT,
        )

    def _build_description(self):
        self._description = ft.Text(
            self._props['description'],
            style="bodyMedium",
            text_align=ft.TextAlign.LEFT,
        )

    def _build_quanty(self):
        self._quantity = ft.Text(
            value=str(self._props['quantity'])
            # , style="headlineMedium"
        )
    
    def _build_quantity_control(self):
        self._quantity_control = ft.Row(
            controls=[
                ft.IconButton(ft.icons.REMOVE, on_click=lambda e: self._update_quantity(e, -1))
                , self._quantity
                , ft.IconButton(ft.icons.ADD, on_click=lambda e: self._update_quantity(e, 1))
            ]
            # , alignment=ft.MainAxisAlignment.START
            # , spacing=5
        )

    def _build_total(self):
        self._total = ft.Text(f"R$ {(self._props['item_value'] * self._props['quantity']):.2f}", style="bodyMedium")

    def _bulid_bottom(self):
        self._build_quanty()
        self._build_quantity_control()
        self._build_total()
        
        self._bottom = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            , spacing=10
            , controls = [
                 self._quantity_control
                , self._total
                , ft.ElevatedButton(
                    text="Pedir"
                    , on_click=lambda _: print("Pedido realizado!")
                    , style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=8)
                    )
                )
            ]
        )