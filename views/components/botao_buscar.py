import flet as ft

def campo_buscar_aluno_(on_change):

    campo = ft.TextField(hint_text="Buscar por nome...",
                         border=ft.InputBorder.NONE,
                         on_change=on_change,
                         expand=True,
                         text_size=20
                         )
    busca = ft.Container(content=ft.Row(controls=[ft.Icon(ft.Icons.SEARCH,
                                                          color="white"),
                                                    campo 
                                                    ],
                                                    spacing=8

                                        ),
                                        width=300,
                                        height=50,
                                        padding=ft.Padding(left=10,
                                                           right=10,
                                                           top=0,
                                                           bottom=0),
                                                           border=ft.Border.all(1,"#dce5f5"),
                                                           border_radius=12
    )

    return busca