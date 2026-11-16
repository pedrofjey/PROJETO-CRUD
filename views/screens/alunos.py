import flet as ft
from ..components import (secao_do_titulo)

def tela_alunos():
    titulo_descricao = secao_do_titulo("Alunos", "Visualize e gerencie os alunos cadastrados.")
        
    tela = ft.Container(content = ft.Column(controls = [titulo_descricao,]),
                        expand = True)
    return tela