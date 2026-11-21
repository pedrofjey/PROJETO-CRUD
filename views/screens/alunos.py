import flet as ft
from ..components import (secao_do_titulo, campo_buscar_aluno,criar_botao, criar_tabela, criar_formulario)
from models.alunos import (alunos, excluir_aluno, editar_aluno, cadastrar_aluno)

#Cria a tela alunos
def tela_alunos(page):
    titulo_descricao = secao_do_titulo("Alunos", "Visualize e gerencie os alunos cadastrados.")

    #Busca o aluno ao digitar e mostra apenas ele na tabela
    pesquisa_atual = ""

    def buscar_aluno(e):
        nonlocal pesquisa_atual
        pesquisa_atual = e.control.value.lower().strip()
        atualizar_tabela()

    #campo de pesquisa do aluno
    campo_pesquisa = campo_buscar_aluno(buscar_aluno)
    
    #Adiciona o titulo, botão cadastrar e campo de pesquisa em uma linha
    linha_titulo_buscar = ft.Row(controls=[titulo_descricao,
                                           ft.Column(controls=[criar_botao("+ Cadastrar Aluno", lambda e: formulario_cadastrar()), campo_pesquisa],
                                                     alignment = ft.MainAxisAlignment.CENTER)],
                                 alignment= ft.MainAxisAlignment.SPACE_BETWEEN)
    
    #Atualiza as linhas da tabela
    def atualizar_tabela():
            tabela.content.rows = criar_linhas()
            page.update()

    #Cria o formulario de cadastro do aluno
    def formulario_cadastrar():

        #Campos do formulario
        campo_nome = ft.TextField(label = "Nome",
                                  hint_text = "Ex.: Ana Siva")
                
        campo_cpf = ft.TextField(label = "CPF",
                                 hint_text = "Ex.: 123.456.789-10")
                    
        campo_email = ft.TextField(label = "Email",
                                   hint_text = "Ex.: nome@email.com")
                    
        campo_idade = ft.TextField(label = "Idade",
                                   hint_text = "Ex.: 14")
                    
        mensagem = ft.Text("", size = 20, color = "red")

        #Lista com os campos do formulario
        campos = [campo_nome, campo_cpf, campo_email, campo_idade]

        #Cadastra o aluno
        def salvar():
            
            #Chama a função para cadastrar o aluno
            resultado = cadastrar_aluno(campo_nome.value,
                                        campo_cpf.value,
                                        campo_email.value,
                                        campo_idade.value)

            #Atualiza a tabela e fecha o formulario caso o aluno seja cadastrado
            if resultado == "sucesso":
                page.pop_dialog()
                atualizar_tabela()
            #Mostra as mensagens de erro, caso haja algum erro no cadastro
            else:
                mensagens = {"campos vazios": "Preencha todos os campos.",
                             "nome invalido": "Digite um nome valido.",
                             "cpf invalido": "CPF invalido.",
                             "cpf existente": "Este CPF já está cadastrado.",
                             "email invalido": "Digite um email valido.",
                             "email existente": "Este email ja está em uso.",
                             "idade invalida": "Idade minima para cadastro: 14 anos."
                             }
                #Atualiza a mensagem de erro de acordo com o erro
                mensagem.value = mensagens.get(resultado,
                                            "Não foi possivel cadastrar o aluno")
                #Atualiza a pagina
                page.update()

        #Cria o formulario
        formulario = criar_formulario("Cadastrar aluno", campos, mensagem, salvar, page)

        #Abre o formulario
        page.show_dialog(formulario)

    #Cria o formulario de excluir aluno
    def formulario_excluir(id_aluno):

        #Fecha o formulario
        def cancelar(e):
            page.pop_dialog()

        #Exclui o aluno e atualiza a tabela
        def confirmacao_excluir(id_aluno):
            excluir_aluno(id_aluno)
            atualizar_tabela()
            page.pop_dialog()

        #Cria o formulario
        formulario = ft.AlertDialog(title = "Deseja mesmo excluir o aluno?",
                                                    scrollable= True,
                                                    content = ft.Row(controls = [ft.Button(content= "Cancelar",
                                                                                           on_click= cancelar),
                                                                     ft.Button(content="Excluir",
                                                                               on_click= lambda e: confirmacao_excluir(id_aluno))],
                                                                     alignment= ft.MainAxisAlignment.END))
        #Abre o formulario
        page.show_dialog(formulario)

    #Cria o formulario de editar aluno
    def formulario_editar(id_aluno):

        #Busca o aluno a ser editado pelo id
        aluno = None
            
        for item in alunos:
            if item["id"] == id_aluno:
                aluno = item
                break
        #Não retorna nada caso não encontre o aluno
        if aluno is None:
            return
                
        #Campos do formulario
        campo_nome = ft.TextField(label = "Nome",
                                  value = aluno["nome"])
        
        campo_cpf = ft.TextField(label = "CPF",
                                 value = aluno["cpf"])
            
        campo_email = ft.TextField(label = "Email",
                                   value = aluno["email"])
            
        campo_idade = ft.TextField(label = "Idade",
                                   value = aluno["idade"])
            
        mensagem = ft.Text("", size = 20, color = "red")

        #Lista dos campos do formulario
        campos = [campo_nome, campo_cpf, campo_email, campo_idade]

        #Salva as edições feitas
        def salvar():
            #Chama a funçao para editar os dados do aluno
            resultado = editar_aluno(id_aluno,
                                     campo_nome.value,
                                     campo_cpf.value,
                                     campo_email.value,
                                     campo_idade.value)
            
            #Fecha o formulario e atualiza a tabela caso as edições sejam realizadas
            if resultado == "sucesso":
                page.pop_dialog()
                atualizar_tabela()
            #Mostra as mensagens caso algum campo apresente algum erro    
            else:
                 mensagens = {"campos vazios": "Preencha todos os campos",
                              "nome invalido": "Digite um nome valido.",
                              "cpf invalido": "CPF invalido.",
                              "cpf existente": "Este CPF já está cadastrado.",
                              "email invalido": "Digite um email valido.",
                              "email existente": "Este email ja está em uso.",
                              "idade invalida": "Idade minima para cadastro: 14 anos."
                              }
                #Atualiza a mensagem de acordo com o erro
                 mensagem.value = mensagens.get(resultado,
                                                "Não foi possivel editar o aluno")
                 #Atualiza a pagina
                 page.update()

        #Cria o formulario
        formulario = criar_formulario("Editar dados do aluno", campos, mensagem, salvar, page)

        #Abre o formulario
        page.show_dialog(formulario)
    
    #Lista com as colunas da tabela alunos
    colunas = [ft.DataColumn(ft.Text("Nome")),
               ft.DataColumn(ft.Text("CPF")),
               ft.DataColumn(ft.Text("Email")),
               ft.DataColumn(ft.Text("Idade")),
               ft.DataColumn(ft.Text("Ações"))]

    #Lista com a linhas da tabela alunos
    def criar_linhas():
        #LInhas da tabela
        linhas = []

        #Veriifca se os alunos digitados no campo buscar existem na tabela pelo nome ou cpf
        for aluno in alunos:
            nome = aluno["nome"].lower()

            cpf = aluno["cpf"].replace(".", "").replace("-", "")

            pesquisa_cpf = pesquisa_atual.replace(".", "").replace("-", "")
            #Se não estiver, a tabela não mostra nenhum aluno
            if pesquisa_atual not in nome and pesquisa_cpf not in cpf:
                continue

            #Cria as linhas com as informaçõs de cada aluno
            linha = ft.DataRow(cells = [ft.DataCell(ft.Text(aluno["nome"])),
                                        ft.DataCell(ft.Text(aluno["cpf"])),
                                        ft.DataCell(ft.Text(aluno["email"])),
                                        ft.DataCell(ft.Text(aluno["idade"])),
                                        ft.DataCell(ft.PopupMenuButton(icon = ft.Icons.MORE_VERT,
                                                                items = [ft.PopupMenuItem("Editar",
                                                                                            on_click = lambda e, id_aluno= aluno["id"]: formulario_editar(id_aluno)),
                                                                        ft.PopupMenuItem("Excluir",
                                                                                            on_click = lambda e, id_aluno = aluno["id"]: formulario_excluir(id_aluno))]))])
            #Adiciona a lista de linhas
            linhas.append(linha)

        return linhas

    #Cria as linhas
    linhas = criar_linhas()

    #Cria a tabela
    tabela = criar_tabela(colunas, linhas)

    #Linha que contem a tabela
    linha_tabela = ft.Row(controls = [tabela],
                          alignment= ft.MainAxisAlignment.SPACE_EVENLY,
                          vertical_alignment = ft.CrossAxisAlignment.START,
                          expand= True)

    #Adiciona a linha do titulo e a linha da tabela ao container da tela
    tela = ft.Container(content = ft.Column(controls =[linha_titulo_buscar, linha_tabela],
                        expand = True))
    return tela