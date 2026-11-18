import flet as ft

def criar_botao(texto, on_click = None):
    botao = ft.Button(content= ft.Text(texto, size = 30),
                      color = "#de8123",
                      on_click = on_click)
    return botao