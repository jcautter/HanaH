import flet as ft

from meta_class.Cardapio import Cardapio
from meta_class.MenuCardapio import MenuCardapio
from meta_class.ItemCardapio import ItemCardapio

def main(page):
    page.title = "Cardapio"

    # menu = ft.Row(
    #     spacing=20,
    #     alignment=ft.MainAxisAlignment.CENTER,
    #     scroll=ft.ScrollMode.AUTO,
    # )

    # cardapio = ft.Column(
    #     expand=True,
    #     spacing=10,
    #     scroll=ft.ScrollMode.AUTO
    # )

    # def scroll_to(key:str, duration=500):
    #     print(key)
    #     cardapio.scroll_to(key=key, duration=duration)

    # menu.controls.append(ft.TextButton('Bebidas'+str(0), on_click=lambda _: scroll_to(key='Bebidas'+str(0))))
    # menu.controls.append(ft.TextButton('Bebidas'+str(1), on_click=lambda _: scroll_to(key='Bebidas'+str(1))))
    # menu.controls.append(ft.TextButton('Bebidas'+str(2), on_click=lambda _: scroll_to(key='Bebidas'+str(2))))
    # menu.controls.append(ft.TextButton('Bebidas'+str(3), on_click=lambda _: scroll_to(key='Bebidas'+str(3))))
    # menu.controls.append(ft.TextButton('Bebidas'+str(4), on_click=lambda _: scroll_to(key='Bebidas'+str(4))))
    # menu.controls.append(ft.TextButton('Bebidas'+str(5), on_click=lambda _: scroll_to(key='Bebidas'+str(5))))
    # menu.controls.append(ft.TextButton('Bebidas'+str(6), on_click=lambda _: scroll_to(key='Bebidas'+str(6))))
    # menu.controls.append(ft.TextButton('Bebidas'+str(7), on_click=lambda _: scroll_to(key='Bebidas'+str(7))))
    # menu.controls.append(ft.TextButton('Bebidas'+str(8), on_click=lambda _: scroll_to(key='Bebidas'+str(8))))
    # menu.controls.append(ft.TextButton('Bebidas'+str(9), on_click=lambda _: scroll_to(key='Bebidas'+str(9))))
    
    # for j in range(10):
    #     cardapio.controls.append(ft.Text('Bebidas'+str(j), style="headlineMedium", key='Bebidas'+str(j)))
    #     for i in range(j*10, j*10+10):
    #         cardapio.controls.append(ItemCardapio('img/Bebida.jpg','Suco de Laranja'+str(i),'Com ou Sem açúcar'+str(i),'R${i},00'.format(i=i),'Adicionar ao Pedido'))
    
    cardapio = Cardapio()
    menu = MenuCardapio(cardapio)

    for j in range(10):
        txt = 'Bebidas'+str(j)
        menu._add_item(txt)
        cardapio._add_title(txt)
        for i in range(j*10, j*10+10):
            cardapio._add_item(
                ItemCardapio(
                    'img/Bebida.jpg'
                    ,'Suco de Laranja'+str(i)
                    ,'Com ou Sem açúcar'+str(i)
                    ,'R${i},00'.format(i=i)
                    ,'Adicionar ao Pedido'
                )
            )
            
    page.add(menu, cardapio)

ft.app(target=main)
