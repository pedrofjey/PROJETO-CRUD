
import flet as ft
from models.cursos import cursos

def card_idioma(nome):
    cursos_do_idioma = [item for item in cursos
                        if item["idioma"] == nome]

    controles_niveis = []

    for nivel in cursos_do_idioma:
        controles_niveis.append(ft.ListTile(title = nivel["nivel"],
                                                            subtitle = f"{nivel["carga_horaria"]} horas - R$ {nivel["preco"]:.2f}"))
    
    card = ft.Container(content = ft.ExpansionTile(title= nome,
                                                   subtitle= f"{len(cursos_do_idioma)} niveis cadastrados",
                                                   expand= True,
                                                   controls = controles_niveis),
                                                   border= ft.Border.all(1, "white"),
                                                   border_radius= 30)
    return card
