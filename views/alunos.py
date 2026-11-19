import flet as ft
from .components import (secao_do_titulo, campo_buscar_aluno_,criar_botao)

def tela_alunos():
    titulo_descricao = secao_do_titulo("Alunos", "Visualize e gerencie os alunos cadastrados.") 
    def buscar_aluno(e):
        pesquisa = e.control.value
        print(pesquisa)

    pesquisa = campo_buscar_aluno_(buscar_aluno)
    
    linha_titulo_buscar = ft.Row(controls=[titulo_descricao,
                                           ft.Column(controls=[criar_botao("+ Cadastrar Aluno"),pesquisa],
                                                     alignment = ft.MainAxisAlignment.CENTER)],
                                 alignment= ft.MainAxisAlignment.SPACE_BETWEEN)
        
    tela = ft.Container(content = ft.Column(controls =[linha_titulo_buscar]),
                        expand = True)
    return tela

