import flet as ft

def criar_botao(texto, on_click = None):
    botao = ft.Button(content= ft.Text(texto, size = 30, weight= ft.FontWeight.BOLD),
                      color = "#d4642c",
                      on_click = on_click)
    return botao