import flet as ft
from ..components import secao_do_titulo

def tela_configuracoes():
    titulo_e_descricao = secao_do_titulo("Configurações", "Personalize a sua experiência no Linguinet")
    
    tema = ft.Container(content = ft.Column(controls=[ft.Text("Tema", size = 40, weight = ft.FontWeight.BOLD),
                                            ft.Row(controls = [ft.IconButton(icon = ft.Icons.SUNNY, icon_color= "#ffae00", icon_size= 100),
                                                               ft.IconButton(icon = ft.Icons.MODE_NIGHT, icon_color= "#140c9f", icon_size= 100)],
                                                               spacing= 10)]),
                                                               border= ft.Border.all(1, ft.Colors.WHITE),
                                                               border_radius=30,
                                                               padding = 5)

    notificacoes = ft.Container(content = ft.Column(controls = [ft.Text("Notificações", size = 40, weight= ft.FontWeight.BOLD),
                                                                ft.Switch(label = "Receber lembretes de notificação", value = False, active_color= "#ffae00", width= 420, height= 60),
                                                                ft.Switch(label = "Avisos de novas aulas", value = False, active_color= "#ffae00", width= 300, height= 60)],
                                                                expand = True),
                                                                border = ft.Border.all(1, "white"),
                                                                border_radius= 30,
                                                                padding= 5)
    
    linhaTemaENotificaçoes = ft.Row(controls = [tema, notificacoes])

    tela = ft.Container(content = ft.Column(controls = [titulo_e_descricao, linhaTemaENotificaçoes]))
    return tela