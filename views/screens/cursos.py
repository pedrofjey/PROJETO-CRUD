import flet as ft
from ..components import (secao_do_titulo, card_idioma, criar_botao)

def tela_cursos():
    titulo_e_descricao = secao_do_titulo("Cursos", "Escolha um idioma para ver os cursos disponíveis")

    linha_titulo_addCurso = ft.Row(controls= [titulo_e_descricao, criar_botao("Adicionar curso")], alignment= ft.MainAxisAlignment.SPACE_BETWEEN)

    card_ingles = card_idioma("Ingles")

    card_espanhol = card_idioma("Espanhol")

    card_frances = card_idioma("Francês")
    
    tela = ft.Container(content = ft.Column(controls = [linha_titulo_addCurso, card_ingles, card_espanhol, card_frances]),
                        expand = True)
    return tela