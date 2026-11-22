import flet as ft
from ..components import (secao_do_titulo, criar_botao, campo_buscar, criar_formulario, criar_tabela)
from models.matriculas import (matriculas, cadastrar_matricula, cancelar_matricula, buscar_matriculas)
from models.alunos import alunos
from models.cursos import cursos

#Cria a tela de matriculas
def tela_matriculas(page):
    #Titulo e descrição da tela
    titulo_descricao = secao_do_titulo("Matriculas", "Confira e gerencie as matriculas dos alunos.")

    #Formulario de cadastro de nova matricula
    def formulario_cadastrar():
        #Campos do formulario
        campo_aluno = ft.Dropdown(label = "Selecione um aluno",
                                  options = [ft.DropdownOption(key = str(aluno["id"]),
                                                             text = aluno["nome"])
                                                             for aluno in alunos])

        campo_curso = ft.Dropdown(label = "Selecione um curso",
                                  options = [ft.DropdownOption(key = str(curso["id"]),
                                                               text=f'{curso["idioma"]} - {curso["nivel"]}')
                                                               for curso in cursos])

        mensagem = ft.Text("", size = 20, color = "red")

        #Lista dos campos do formulario
        campos = [campo_aluno, campo_curso]

        #Cadastra a matricula
        def salvar():
            #Verifica se os campos foram preenchidos
            if not campo_aluno.value or not campo_curso.value:
                mensagem.value = "Selecione um aluno e um curso"
                page.update()
                return
            
            #Chama a função de cadastro
            resultado = cadastrar_matricula(int(campo_aluno.value), int(campo_curso.value))

            #Mensagens de erro
            mensagens = {"sucesso": "Matrícula cadastrada!",
                         "duplicado": "Esse aluno já está matriculado nesse curso.",
                         "nivel existente": "Esse aluno já está matriculado nesse idioma em outro nível.",
                         "inexistente": "Aluno ou curso não encontrado."
                         }

            #Atualiza a mensagem de acordo com o erro
            mensagem.value = mensagens[resultado]

            #Fecha e atualiza a tabela caso o cadastro der certo
            if resultado == "sucesso":
                page.pop_dialog()
                atualizar_tabela()
            else:
                page.update()

        #Cria o formulario
        formulario = criar_formulario("Nova Matricula", campos, mensagem, salvar, page)
        #Abre o formulario
        page.show_dialog(formulario)

    #Variavel que conterá os valores digitados no campo buscar
    pesquisa_atual = ""
    #Busca a maricula e ostra na tabela
    def buscar(e):
        nonlocal pesquisa_atual
        pesquisa_atual = e.control.value.lower().strip()
        atualizar_tabela()

    #Atualiza a tabela
    def atualizar_tabela():
        tabela.content.rows = criar_linhas()
        page.update()

    #Campo de pesquisa de matricula
    campo_pesquisa = campo_buscar(buscar)

    #Linha com titulo, descrição, botão nova matricula e campo de busca de matricula
    linha_titulo_buscar = ft.Row(controls=[titulo_descricao,
                                       ft.Column(controls=[criar_botao("+ Nova Matricula", lambda e: formulario_cadastrar()), campo_pesquisa],
                                                 alignment = ft.MainAxisAlignment.CENTER)],
                             alignment= ft.MainAxisAlignment.SPACE_BETWEEN)

    #Colunas da tabela
    colunas = [ft.DataColumn(ft.Text("Aluno")),
               ft.DataColumn(ft.Text("Idioma")),
               ft.DataColumn(ft.Text("Nivel")),
               ft.DataColumn(ft.Text("Status")),
               ft.DataColumn(ft.Text("Ações"))]

    #Tabela
    tabela = criar_tabela(colunas, [])

    #Linha que contem a tabela
    linha_tabela = ft.Row(controls = [tabela],
                          alignment= ft.MainAxisAlignment.SPACE_EVENLY,
                          vertical_alignment = ft.CrossAxisAlignment.START,
                          expand= True)

    #Cancela a matricula
    def cancelar(id_matricula):

        resultado = cancelar_matricula(id_matricula)

        if resultado == "sucesso":
            atualizar_tabela()


    #Cria linhas da tabela
    def criar_linhas():
        #Lista de linhas vazia
        linhas = []
        #Altera a matricula mostrada na tabela de acordo com o que é digitado no campo buscar
        if pesquisa_atual:
            resultados = buscar_matriculas(pesquisa_atual)
        else:
            resultados = matriculas

        for item in resultados:

            aluno_matriculado = None
            curso_matriculado = None

            #Busca o aluno
            for aluno in alunos:
                if aluno["id"] == item["id_aluno"]:
                    aluno_matriculado = aluno
                    break

            #Busca o curso
            for curso in cursos:
                if curso["id"] == item["id_curso"]:
                    curso_matriculado = curso
                    break

            if aluno_matriculado is None or curso_matriculado is None:
                continue
            
            acao = (ft.Button(content = ft.Text("Cancelar",
                                          color = "red",
                                          size = 16),
                                          bgcolor = "#879fbd",
                    on_click=lambda e, id_matricula=item["id"]: cancelar(id_matricula))
                    if item["status"] == "Ativa"
                    else ft.Text("-"))
            #Cria a linha
            linha = ft.DataRow(cells = [ft.DataCell(ft.Text(aluno_matriculado["nome"])),
                                        ft.DataCell(ft.Text(curso_matriculado["idioma"])),
                                        ft.DataCell(ft.Text(curso_matriculado["nivel"])),
                                        ft.DataCell(ft.Text(item["status"])),
                                        ft.DataCell(acao)])
            linhas.append(linha)
        return linhas

    tabela.content.rows = criar_linhas()
    
    #Tela completa
    tela = ft.Container(content = ft.Column(controls = [linha_titulo_buscar, linha_tabela]),
                        expand = True)
    return tela