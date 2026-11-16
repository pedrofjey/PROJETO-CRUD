import flet as ft

def secao_do_titulo(titulo, descricao):
    tituloESubtitulo = ft.Column(controls = [ft.Text(titulo, size = 50, weight = ft.FontWeight.BOLD),
                                             ft.Text(descricao, size = 20, weight = ft.FontWeight.BOLD)],
                                             spacing= 5)
    return tituloESubtitulo