import flet as ft
from ..components import (secao_do_titulo, card_idioma, criar_botao, criar_formulario)
from models.cursos import (cursos, cadastrar_curso)

#Cria a tela cursos
def tela_cursos(page):
    titulo_e_descricao = secao_do_titulo("Cursos", "Escolha um idioma para ver os cursos disponíveis")

    lista_cards = ft.Column()

    #Atualiza os cards da pagina
    def atualizar_cards():
        lista_cards.controls = [card_idioma("Inglês", page, atualizar_cards),
                                card_idioma("Espanhol",page, atualizar_cards),
                                card_idioma("Francês", page, atualizar_cards)]
    #Já começa atualizada com os cards
    atualizar_cards()

    #Abre o formulario de cadastro de curso
    def formulario_cadastrar(e):

        #Campos do formulario
        campo_idioma = ft.Dropdown(label= "Selecione um idioma",
                                   options=[ft.DropdownOption("Inglês"),
                                            ft.DropdownOption("Espanhol"),
                                            ft.DropdownOption("Francês")])

        campo_nivel = ft.Dropdown(label = "Selecione um nivel",
                                  options= [ft.DropdownOption("Básico"),
                                            ft.DropdownOption("Intermediário"),
                                            ft.DropdownOption("Avançado")])

        campo_carga_horaria = ft.TextField(label = "Carga horária",
                                           hint_text= "Ex.: 40")

        campo_preco = ft.TextField(label = "Preço",
                                   hint_text= "Ex.: 150.00")

        mensagem = ft.Text("", color = "red", size = 20)

        #Lista com os campos do cadastro
        campos = [campo_idioma, campo_nivel, campo_carga_horaria, campo_preco]

        #Cadastra o curso e atualiza os cards
        def salvar():
            idioma = campo_idioma.value
            nivel = campo_nivel.value
            carga = campo_carga_horaria.value
            preco = campo_preco.value

            #Verifica se todos os campos foram preenchidos
            if not idioma or not nivel or not carga or not preco:
                mensagem.value = "Preencha todos os dados!"
                mensagem.color = "yellow"
                return 

            #Chama a função para cadastrar o curso
            rerultado = cadastrar_curso(idioma, nivel, carga, preco)

            #Atualiza os cursos caso seja cadastrado
            if rerultado == "sucesso":
                mensagem.value = "Curso cadastrado!"
                mensagem.color = "green"
                atualizar_cards()
                page.pop_dialog()
                page.update()
            #Verifica se o curso ja existe
            elif rerultado == "duplicado":
                mensagem.value = "Esse curso já existe!"
            #Verifica se a carga é valida
            elif rerultado == "carga_invalida":
                mensagem. value = "Carga horária invalida!"
            #Verifica se o preço é valido
            elif rerultado == "preco_invalido":
                mensagem.value = "Preço invalido!"
        
        #Cria o formulario de cadastro
        formulario = criar_formulario("Cadastrar curso", campos, mensagem, salvar, page)

        #Abre o formulario
        page.show_dialog(formulario)

    #Cria a linha com o titulo e o botão de cadastrar curso
    linha_titulo_addCurso = ft.Row(controls= [titulo_e_descricao, criar_botao("+ adicionar curso", formulario_cadastrar)],
                                   alignment= ft.MainAxisAlignment.SPACE_BETWEEN)
    
    #tela completa
    tela = ft.Container(content = ft.Column(controls = [linha_titulo_addCurso, lista_cards]),
                        expand = True)
    return tela