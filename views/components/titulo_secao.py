import flet as ft

#Cria a coluna com o titulo e o subtitulo de cada tela
def secao_do_titulo(titulo, descricao):
    tituloESubtitulo = ft.Column(controls = [ft.Text(titulo, size = 50, weight = ft.FontWeight.BOLD),
                                             ft.Text(descricao, size = 20, weight = ft.FontWeight.BOLD)],
                                             spacing= 5)
    return tituloESubtitulo