import flet as ft
import views as vi

def main(page: ft.Page):
    page.title = "Linguinet - Cursos de Idiomas"
    page.window.maximizable = True
    page.theme_mode = ft.ThemeMode.DARK

    cursos = ft.NavigationDrawerDestination(label = "Cursos", icon = ft.Icons.BOOK_OUTLINED,selected_icon = ft.Icons.BOOK)

    matriculas = ft.NavigationDrawerDestination(label = "Matriculas", icon = ft.Icons.CALENDAR_MONTH_OUTLINED,selected_icon = ft.Icons.CALENDAR_MONTH)

    alunos = ft.NavigationDrawerDestination(label = "Alunos", icon = ft.Icons.PEOPLE_ALT_OUTLINED,selected_icon = ft.Icons.PEOPLE_ALT)

    configuracoes = ft.NavigationDrawerDestination(label = "Configurações", icon = ft.Icons.SETTINGS_OUTLINED,selected_icon = ft.Icons.SETTINGS)

    telas = {0: vi.tela_cursos(page),
            1: vi.tela_matriculas(),
            2: vi.tela_alunos(),
            3: vi.tela_configuracoes()
    }

    conteudo = ft.Container(content= telas[0],
                            expand= True)

    def mudanca_de_tela(e):
        conteudo.content = telas[e.control.selected_index]
        page.update()
            
    menu = ft.NavigationDrawer(controls = [ft.Text("LINGUINET", size = 30, align= ft.Alignment.CENTER), cursos, matriculas, alunos, configuracoes],
                                selected_index = 0,
                                width = 240,
                                expand = False,
                                indicator_color= "#d4642c",
                                bgcolor = "#001649",
                                on_change= mudanca_de_tela)

    linhaTela = ft.Row(controls= [menu, conteudo], expand= True)
    
    page.add(linhaTela)

ft.run(main)