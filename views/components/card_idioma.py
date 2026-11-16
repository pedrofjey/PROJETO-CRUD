
import flet as ft


def card_idioma(nome):
    card = ft.Container(content = ft.ExpansionTile(title= nome,
                                                   subtitle= "3 niveis cadastrados",
                                                   expand= True,
                                                   controls = [ft.ListTile(title = "basico"),
                                                               ft.ListTile(title = "Intermediário"),
                                                               ft.ListTile(title = "Avançado")]),
                                                   border= ft.Border.all(1, "white"),
                                                   border_radius= 30)
    return card
