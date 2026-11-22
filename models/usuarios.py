#Lista de usuarios cadastrados
usuarios = []

#Cadastrar usuario
def cadastrar_usuario(nome, email, senha):
    # Verifica se o nome contém apenas letras
    if not nome.replace(" ", "").isalpha():
        return "nome invalido"
    
    #Verifica se o email e valido
    if "@" not in email or "." not in email:
        return "email invalido"
    
    #verifica se o email já está cadastrado
    for usuario in usuarios:
        if usuario["email"] == email:
            return "email existente"

    # Verifica o tamanho da senha
    if len(senha) < 6:
        return "senha invalida"

    #Cria o usuario
    novo_usuario = {"id": len(usuarios) + 1,
                    "nome": nome,
                    "email": email,
                    "senha": senha
                    }

    usuarios.append(novo_usuario)

    return "sucesso"

#Valida o login
def validar_login(email, senha):
    #Busca o usuario cadastrado
    for usuario in usuarios:
        if usuario["email"] == email and usuario["senha"] == senha:
            return usuario

    return None