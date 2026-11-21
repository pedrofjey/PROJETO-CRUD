#Lsta de alunos cadastrados
alunos = [{"id": 1,
           "nome": "Pedro Henrique",
           "cpf": "168.488.224.93",
           "email": "pehh3435@gmail.com",
           "idade": "15"
           }]

#Validação do cpf
def validacao_cpf(cpf):

    #Retira os pontos e ifens do cpf
    cpf = cpf.replace(".", "").replace("-", "").strip()

    #Verifica quantidade de digitos
    if len(cpf) != 11 or not cpf.isdigit():
        return False
    
    #Verifica se são numeros reptidos
    if cpf == cpf[0] * 11:
        return False

    # Primeiro dígito verificador
    soma = 0

    #Calcula os 9 primeiros digitos para saber se o cpf é valido
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)

    resultado = (soma * 10) % 11

    if resultado == 10:
        resultado = 0

    if resultado != int(cpf[9]):
        return False

    # Segundo dígito verificador
    soma = 0

    #Calcula os 2 ultimos digitos para saber se o cpf é valido
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)

    resultado = (soma * 10) % 11

    if resultado == 10:
        resultado = 0

    if resultado != int(cpf[10]):
        return False

    return True

#Procura o aluno pelo id e exclui
def excluir_aluno(id_aluno):
    for aluno in alunos:
        if aluno["id"] == id_aluno:
            alunos.remove(aluno)
            return "sucesso"
    else:
        return "falha"

#Edita os dados do aluno
def editar_aluno(id_aluno, novo_nome, novo_cpf, novo_email, nova_idade):

    #Verifica o id do aluno a ser editado
    for aluno in alunos:
        if aluno["id"] == id_aluno:

            #Verifica se tem campos vazios
            if not novo_nome.strip() or not novo_cpf.strip() or not novo_email.strip() or not nova_idade.strip():
                return "campos vazios"

            #Verificar se foi digitado um nome
            if not novo_nome.strip():
                return "nome invalido"

            #Verifica se foi digitado algum numero no nome
            for letra in novo_nome:
                if letra.isdigit():
                    return "nome invalido"

            #Verifica se o cpf é valido
            if not validacao_cpf(novo_cpf):
                return "cpf invalido"

            #Verifica se o cpf ja está cadastrado
            for outro in alunos:
                cpf_cadastrado = outro["cpf"].replace(".", "").replace("-", "").strip()
                cpf = novo_cpf.replace(".", "").replace("-", "").strip()

                if cpf_cadastrado == cpf and outro["id"] != id_aluno:
                    return "cpf existente"

            #Verifica se o email é valido
            if "@" not in novo_email or "." not in novo_email:
                return "email invalido"

            #Verifica se o email ja está cadastrado
            for outro in alunos:
                if outro["email"] == novo_email and outro["id"] != id_aluno:
                    return "email duplicado"

            #Verifica se a idade é valida
            try:
                idade = int(nova_idade)
                if idade <14:
                    return "idade invalida"
            except ValueError:
                return "cpf invalido"

            #Atualiza os dados do aluno
            aluno["nome"] = novo_nome
            aluno["cpf"] = novo_cpf
            aluno["email"] = novo_email
            aluno["idade"] = idade

            return "sucesso"
    return "falha"

#Cadastra novos alunos
def cadastrar_aluno(nome, cpf, email, idade):

    #Verifica se tem campos vazios
    if not nome.strip() or not cpf.strip() or not email.strip() or not idade.strip():
        return "campos vazios"

    #Verifica se tem algum numero no nome
    if any(numero.isdigit() for numero in nome):
        return "nome invalido"

    #Verifica se o nome foi preenchido
    if not nome.strip():
        return "nome invalido"

    #Verifica se o cpf é valido calculando os digitos
    if not validacao_cpf(cpf):
        return "cpf invalido"
    
    #Tira os pontos e ifens do cpf para poder validar
    cpf_limpo = cpf.replace(".", "").replace("-", "").strip()

    #Verifica se o cpf ja está cadastrado
    for aluno in alunos:
        cpf_cadastrado = aluno["cpf"].replace(".", "").replace("-", "").strip()

        if cpf_cadastrado == cpf:
            return "cpf existente"

    #Verifica se o email é valido
    if "@" not in email or "." not in email:
        return "email invalido"

    #Tira os espaços extras do email e verifica se ja está cadastrado
    email = email.strip()

    for aluno in alunos:
        if aluno["email"].lower() == email.lower():
            return "email existente"

    #Verifica se a idade é valida
    try:
        idade = int(idade)
    except ValueError:
        return "idade invalida"

    if idade < 14:
        return "idade invalida"

    #Formata o cpf para que tenha os pontos e ifens antes de cadastrar
    cpf_formatado = (f"{cpf_limpo[:3]}."
                     f"{cpf_limpo[3:6]}."
                     f"{cpf_limpo[6:9]}-"
                     f"{cpf_limpo[9:]}")

    #Salva os dados do novo aluno
    novo_aluno = {"id": len(alunos) + 1,
           "nome": nome.strip(),
           "cpf": cpf_formatado,
           "email": email,
           "idade": idade
           }

    #Adiciona o novo aluno a lista de alunos
    alunos.append(novo_aluno)

    return "sucesso"