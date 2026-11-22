import flet as ft

#Cria a tabela que contem as informações dos alunos
def criar_tabela(colunas,linhas):
    #Tabela
    tabela = ft.DataTable(columns=colunas,
                          rows=linhas,
                          heading_row_color="#172B4D",
                          heading_text_style=ft.TextStyle(color= "white",
                                                          size = 16,
                                                          weight=ft.FontWeight.BOLD),
                          data_text_style=ft.TextStyle(color= "white",
                                                       size = 16),
                          border= ft.Border.all(1, "#334155"),
                          border_radius= 12,
                          divider_thickness= 0.5)

    #container que contem a tabela
    container = ft.Container(content=tabela,
                             border_radius=15,
                             bgcolor= "#93aece",
                             opacity=0.6,
                             expand= True)
    
    return container