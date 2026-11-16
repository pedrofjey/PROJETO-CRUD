import flet as ft

def criar_botao(texto):
    botao = ft.Button(content= ft.Text(texto, size = 30), color = "#de8123")
    return botao