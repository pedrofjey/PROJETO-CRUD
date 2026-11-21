import flet as ft
from ..components import (secao_do_titulo)

def tela_matriculas(page):
    titulo_descricao = secao_do_titulo("Matriculas", "Confira e gerencie as matriculas dos alunos.")
        
    tela = ft.Container(content = ft.Column(controls = [titulo_descricao,]),
                        expand = True)
    return tela