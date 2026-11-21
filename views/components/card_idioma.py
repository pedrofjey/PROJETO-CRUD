
import flet as ft
from models.cursos import (cursos, editar_curso, excluir_curso)

#Cria o card com os niveis de cada idioma
def card_idioma(nome, page, atualizar_cards):

    #Busca os cursos do idioma
    cursos_do_idioma = [item for item in cursos
                        if item["idioma"] == nome]

    #lista das linhas dos niveis de cada curso
    controles_niveis = []

    #Cria o formulario de edição do curso
    def formulario_editar(nivel):

        #Campos do formulario
        campo_carga_horaria = ft.TextField(label = "Carga horária",
                                           hint_text= "Ex.: 40")

        campo_preco = ft.TextField(label = "Preço",
                                   hint_text= "Ex.: 150.00")

        mensagem = ft.Text("", size = 20)

        #Fecha o formulario
        def cancelar(e):
            page.pop_dialog()

        #Verifica e edita as informações do curso
        def salvar(e):
            carga = campo_carga_horaria.value
            preco = campo_preco.value

            if not carga or not preco:
                mensagem.value = "Preencha todos os dados!"
                mensagem.color = "yellow"
                return 
            
            rerultado = editar_curso(nivel["id"],carga, preco)

            if rerultado == "sucesso":
                mensagem.value = "Curso editado!"
                mensagem.color = "green"
                atualizar_cards()
                page.pop_dialog()
                page.update()
            elif rerultado == "carga_invalida":
                mensagem. value = "Carga horária invalida!"
            elif rerultado == "preco_invalido":
                mensagem.value = "Preço invalido!"

        #Formulario
        formulario = ft.AlertDialog(title = "Editar curso",
                                    scrollable= True,
                                    content = ft.Column(controls = [campo_carga_horaria, campo_preco, mensagem,
                                                                    ft.Row(controls = [ft.Button(content= "Cancelar",
                                                                                                 on_click= cancelar),
                                                                                        ft.Button(content="Salvar",
                                                                                                  on_click= salvar)],
                                                                                        alignment= ft.MainAxisAlignment.END)]))
        #Abre o formulario
        page.show_dialog(formulario)

    #Mostra um formulario para confirmação de exclusão do curso
    def formulario_excluir(nivel):
        #Fecha o formulario
        def cancelar():
            page.pop_dialog()

        #Exclui o curso
        def excluir():
            excluir_curso(nivel)
            atualizar_cards()
            page.pop_dialog()
            page.update()

        #formulario
        formulario = ft.AlertDialog(title = "Deseja mesmo excluir o curso?",
                                            scrollable= True,
                                            content = ft.Row(controls = [ft.Button(content= "Cancelar",
                                                                                   on_click= cancelar),
                                                                         ft.Button(content="Excluir",
                                                                                   on_click= excluir)],
                                                             alignment= ft.MainAxisAlignment.END))
        page.show_dialog(formulario)

    #Cria a as linhas contendo as informações de cada nivel
    for nivel in cursos_do_idioma:
        linha = ft.Row(controls = [ft.Column(controls = [ft.Text(nivel["nivel"], size = 15),
                                                         ft.Text(f"{nivel["carga_horaria"]} horas - "
                                                                 f"R$ {nivel['preco']:.2f}")]),
                        ft.Row(controls = [ft.IconButton(icon = ft.Icons.EDIT,
                                           tooltip= "Editar curso",
                                           icon_color= "green",
                                           on_click= lambda e: formulario_editar(nivel)),
                        ft.IconButton(icon = ft.Icons.DELETE,
                                      icon_color= "red",
                                      tooltip= "Excluir curso",
                                      on_click= lambda e: formulario_excluir(nivel["id"]))])],
                        alignment= ft.MainAxisAlignment.SPACE_BETWEEN)
        #Adiciona a lista
        controles_niveis.append(linha)

    #Cria o card do idioma
    card = ft.Container(content = ft.ExpansionTile(title= ft.Text(nome, size = 20),
                                                   subtitle= f"{len(cursos_do_idioma)} niveis cadastrados",
                                                   expand= True,
                                                   controls = controles_niveis,
                                                   shape=ft.RoundedRectangleBorder(radius=0),
                                                   collapsed_shape=ft.RoundedRectangleBorder(radius=0)),
                                                   border= ft.Border.all(1, "white"),
                                                   border_radius= 30,
                                                   padding = 8)
    return card