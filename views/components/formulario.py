import flet as ft

#Cria os formularios utilizados nas telas
def criar_formulario(titulo, campos, mensagem, on_salvar, page):

    #Fecha o formulario
    def cancelar(e):
        page.pop_dialog()
    
    #Formulario
    formulario = ft.AlertDialog(title = titulo,
                                            scrollable= True,
                                            content = ft.Column(controls = [*campos,
                                                                         mensagem,
                                                             ft.Row(controls = [ft.Button(content= "Cancelar",
                                                                                   on_click= cancelar),
                                                             ft.Button(content="Salvar",
                                                                       on_click= lambda e: on_salvar())],
                                                             alignment= ft.MainAxisAlignment.END)]))
    return formulario