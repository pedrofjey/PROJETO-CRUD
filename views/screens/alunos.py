import flet as ft
from ..components import (secao_do_titulo, campo_buscar_aluno_,criar_botao, criar_tabela)

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

    colunas = [ft.DataColumn(ft.Text("Nome")),
               ft.DataColumn(ft.Text("CPF")),
               ft.DataColumn(ft.Text("E-mail")),
               ft.DataColumn(ft.Text("Telefone")),
               ft.DataColumn(ft.Text("Ações"))]

    linhas = [ft.DataRow(cells =
                        [ft.DataCell(ft.Text("Ana souza")),
                         ft.DataCell(ft.Text("000.000.000.00")),
                         ft.DataCell(ft.Text("ana@email.com")),
                         ft.DataCell(ft.Text("(81) 99999-9999")),
                         ft.DataCell(ft.Text("Editar"))])]

    linha_tabela = ft.Row(controls = [criar_tabela(colunas, linhas)],
                          alignment= ft.MainAxisAlignment.SPACE_EVENLY,
                          expand= True)
    
    tela = ft.Container(content = ft.Column(controls =[linha_titulo_buscar, linha_tabela],
                        expand = True))
    return tela