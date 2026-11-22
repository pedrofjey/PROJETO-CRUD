import flet as ft
from models.usuarios import (usuarios, validar_login)
from ..components import criar_botao

#Cria a tela de login
def tela_login(page, abrir_cadastro, login_sucesso):
    #Campos do login
    campo_email = ft.TextField(label = "Email",
                               prefix_icon = ft.Icons.EMAIL,
                               width = 350)

    campo_senha = ft.TextField(label = "Senha",
                               password=True,
                               can_reveal_password=True,
                               prefix_icon=ft.Icons.LOCK,
                               width=350)

    #Mensagem de validação
    mensagem = ft.Text("", color="red", size=14)

    #Função para entrar
    def entrar(e):
        email = campo_email.value.strip().lower()
        senha = campo_senha.value

        #Verifica campos vazios
        if not email or not senha:
            mensagem.value = "Preencha todos os campos."

        else:
            usuario = validar_login(email, senha)

            #Verifica se o login é válido
            if usuario is not None:
                mensagem.value = ""
                login_sucesso(usuario)

            else:
                mensagem.value = "E-mail ou senha incorretos."

        page.update()

    #Logo
    logo = ft.Image(src="logo.jpeg",
                    width=110,
                    height=110)

    #Titulo
    titulo = ft.Text("Bem-vindo ao Linguinet",
                     size = 30,
                     weight = ft.FontWeight.BOLD,
                     color = "white")

    #Descrição
    descricao = ft.Text("Entre na sua conta para continuar.",
                        size=16,
                        color="#B0B0B0")

    #Botão entrar
    botao_entrar = criar_botao("Entrar", entrar)

    #Botão cadastrar
    botao_cadastrar = ft.TextButton("Não tem uma conta? Cadastre-se",
                                    on_click = abrir_cadastro)

    #Card de login
    card = ft.Container(content = ft.Column(controls = [logo,
                                                        titulo,
                                                        descricao,
                                                        campo_email,
                                                        campo_senha,
                                                        mensagem,
                                                        botao_entrar,
                                                        botao_cadastrar],
                                            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                                            spacing = 20,
                                            tight = True),
                        width = 450,
                        padding = 40,
                        bgcolor = "#001649",
                        border_radius = 20)

    #Tela
    tela = ft.Container(content = card,
                        alignment=ft.Alignment.CENTER,
                        expand=True,
                        bgcolor = "#011033")

    return tela