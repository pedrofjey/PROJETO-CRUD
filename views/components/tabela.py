import flet as ft

def criar_tabela(colunas,linhas):
    tabela = ft.DataTable(columns=colunas,
                          rows=linhas,
                          heading_row_color="#172B4D",
                          data_text_style=ft.TextStyle(color="#F1F5F9",
                                                       size=13),
                          heading_text_style=ft.TextStyle(color="#ffffff",
                                                          weight=ft.FontWeight.BOLD),
                          border= ft.Border.all(1, "#334155"),
                          border_radius= 12,
                          divider_thickness= 0.5)

    container = ft.Container(content=tabela,
                             border_radius=15,
                             bgcolor= "#93aece",
                             opacity=0.6,
                             expand= True)
    
    return container