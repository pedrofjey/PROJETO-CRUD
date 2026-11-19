import flet as ft
from ..components import (secao_do_titulo, card_idioma, criar_botao)
from models.cursos import (cursos, cadastrar_curso)

def tela_cursos(page):
    titulo_e_descricao = secao_do_titulo("Cursos", "Escolha um idioma para ver os cursos disponíveis")

    lista_cards = ft.Column()


    def atualizar_cards():
        lista_cards.controls = [card_idioma("Inglês"), card_idioma("Espanhol"), card_idioma("Francês")]

    atualizar_cards()

    def abrir_formulario(e):
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

        def cancelar(e):
            page.pop_dialog()

        def salvar(e):
            idioma = campo_idioma.value
            nivel = campo_nivel.value
            carga = campo_carga_horaria.value
            preco = campo_preco.value

            if not idioma or not nivel or not carga or not preco:
                mensagem.value = "Preencha todos os dados!"
                mensagem.color = "yellow"
                return 
            
            rerultado = cadastrar_curso(idioma, nivel, carga, preco)

            if rerultado == "sucesso":
                mensagem.value = "Curso cadastrado!"
                mensagem.color = "green"
                atualizar_cards()
                page.pop_dialog()
                page.update()
            elif rerultado == "duplicado":
                mensagem.value = "Esse curso já existe!"
            elif rerultado == "carga_invalida":
                mensagem. value = "Carga horária invalida!"
            elif rerultado == "preco_invalido":
                mensagem.value = "Preço invalido!"
        
        formulario = ft.AlertDialog(title = "Novo Curso",
                                    scrollable= True,
                                    content = ft.Column(controls = [campo_idioma, campo_nivel, campo_carga_horaria, campo_preco, mensagem,
                                                                    ft.Row(controls = [ft.Button(content= "Cancelar",
                                                                                                 on_click= cancelar),
                                                                                        ft.Button(content="Salvar",
                                                                                                  on_click= salvar)],
                                                                                        alignment= ft.MainAxisAlignment.END)]))
        page.show_dialog(formulario)

    linha_titulo_addCurso = ft.Row(controls= [titulo_e_descricao, criar_botao("+ adicionar curso", abrir_formulario)],
                                   alignment= ft.MainAxisAlignment.SPACE_BETWEEN)
    
    tela = ft.Container(content = ft.Column(controls = [linha_titulo_addCurso, lista_cards]),
                        expand = True)
    return tela