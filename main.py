import flet as ft
import views as vi

#Pagina do flet
def main(page: ft.Page):
    #
    page.title = "Linguinet - Cursos de Idiomas"
    page.window.maximizable = True
    page.theme_mode = ft.ThemeMode.DARK
    page.window.resizable = True

    #Botões do menu
    cursos = ft.NavigationDrawerDestination(label = "Cursos",
                                            icon = ft.Icons.BOOK_OUTLINED,
                                            selected_icon = ft.Icons.BOOK)

    matriculas = ft.NavigationDrawerDestination(label = "Matriculas",
                                                icon = ft.Icons.CALENDAR_MONTH_OUTLINED,
                                                selected_icon = ft.Icons.CALENDAR_MONTH)

    alunos = ft.NavigationDrawerDestination(label = "Alunos",
                                            icon = ft.Icons.PEOPLE_ALT_OUTLINED,
                                            selected_icon = ft.Icons.PEOPLE_ALT)

    #Dicionario com todas as telas
    telas = {0: vi.tela_cursos(page),
            1: vi.tela_matriculas(page),
            2: vi.tela_alunos(page),
    }

    #Container que ira mostrar cada tela
    conteudo = ft.Container(content= telas[0],
                            expand= True)

    #Muda a tela mostrada de acordo com o menu
    def mudanca_de_tela(e):
        conteudo.content = telas[e.control.selected_index]
        page.update()

    #Menu lateral
    menu = ft.NavigationDrawer(controls = [ft.Image(src = "logo.jpeg",
                                                    width = 100,
                                                    height = 100),
                                           ft.Text("LINGUINET",
                                                    size = 30,
                                                    align= ft.Alignment.CENTER),
                                           ft.Text("Cursos de idiomas",
                                                   size = 15,
                                                   align = ft.Alignment.CENTER),
                                           cursos, matriculas, alunos],
                                selected_index = 0,
                                width = 240,
                                expand = False,
                                indicator_color= "#d4642c",
                                bgcolor = "#001649",
                                on_change= mudanca_de_tela)

    #Linha com o menu e a tela
    linhaTela = ft.Row(controls= [menu, conteudo], expand= True)

    #Adiciona a linha a pagina do flet
    page.add(linhaTela)

#Executa o flet
ft.run(main)