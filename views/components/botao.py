import flet as ft

#Cria o botão que é usado em todas as telas
def criar_botao(texto, on_click = None):
    botao = ft.Button(content= ft.Text(texto, size = 30, weight= ft.FontWeight.BOLD),
                      color = "#d4642c",
                      on_click = on_click)
    return botao