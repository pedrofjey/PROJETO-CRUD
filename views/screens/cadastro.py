import flet as ft
from models.usuarios import (usuarios,cadastrar_usuario)
from ..components import criar_botao

#Cria a tela de cadastro
def tela_cadastro(page, voltar_login):
    #Campos do cadastro
    campo_nome = ft.TextField(label = "Nome completo",
                              prefix_icon = ft.Icons.PERSON,
                              width = 350)

    campo_email = ft.TextField(label = "Email",
                               prefix_icon = ft.Icons.EMAIL,
                               width = 350)

    campo_senha = ft.TextField(label = "Senha",
                               password = True,
                               can_reveal_password = True,
                               prefix_icon = ft.Icons.LOCK,
                               width = 350)

    #mensagem de validação
    mensagem = ft.Text("", color = "red", size = 14)

    #Cadastra o usuario
    def cadastrar(e):
        nome = campo_nome.value.strip()
        email = campo_email.value.strip().lower()
        senha = campo_senha.value

        #Verifica campos vazios
        if not nome or not email or not senha:
            mensagem.value = "Preencha todos os campos"

        else:
            resultado = cadastrar_usuario(nome, email, senha)

            if resultado == "email existente":
                mensagem.value = "Esse email já está cadastrado."

            elif resultado == "email invalido":
                mensagem.value = "Digite um email valido"

            elif resultado == "nome invalido":
                mensagem.value = "Digite um nome valido, usando apenas letras"

            elif resultado == "senha invalida":
                mensagem.value = "A senha deve ter pelo menos 6 caracteres"

            elif resultado == "sucesso":
                mensagem.value = "Cadastro realizado com sucesso!"
                mensagem.color = "green"
                campo_nome.value = "" 
                campo_email.value = ""
                campo_senha.value = ""

            page.update()

    # Logo do Linguinet
    logo = ft.Image(src="logo.jpeg",
                    width=110,
                    height=110)

    #Titulo
    titulo = ft.Text("Criar conta",
                     size = 30,
                     weight = ft.FontWeight.BOLD,
                     color = "white")

    #Descrição
    descricao = ft.Text("Cadastre-se para acessar o Linguinet.",
                        size = 16,
                        color = "#b0b0b0")

    #Botão cadastrar
    botao_cadastrar = criar_botao("Cadastrar", cadastrar)

    #Botão voltar para login
    botao_voltar = ft.TextButton("Já tem uma conta? Entrar", on_click = voltar_login)

    # Card de cadastro
    card = ft.Container(content=ft.Column(controls=[logo,
                                                    titulo,
                                                    descricao,
                                                    campo_nome,
                                                    campo_email,
                                                    campo_senha,
                                                    mensagem,
                                                    botao_cadastrar,
                                                    botao_voltar],
                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                            spacing=20,
                                            tight=True),
                                width=450,
                                padding=40,
                                bgcolor = "#001649",
                                border_radius=20)

    #Tela
    tela = ft.Container(content=card,
                        alignment=ft.Alignment.CENTER,
                        expand=True,
                        bgcolor = "#011033")

    return tela