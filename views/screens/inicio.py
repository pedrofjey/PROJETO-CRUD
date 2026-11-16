import flet as ft
from ..components import (secao_do_titulo)

adm = "Pedro"

def tela_inicio():
    titulo_descricao = secao_do_titulo(f"Bem-vindo, {adm}!", "Gerencie os cursos e matriculas do Linguinet.")
        
    tela = ft.Container(content = ft.Column(controls = [titulo_descricao]),
                        expand = True)
    return tela