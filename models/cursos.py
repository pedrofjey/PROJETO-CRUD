#lista de cursos cadastrados
cursos = [{"id": 1,
          "idioma": "Inglês",
          "nivel": "Básico",
          "carga_horaria": 40,
          "preco": 150.00
          }]

#Verifica se o curso ja existe
def verificar_curso(idioma, nivel):
    for curso in cursos:
        if idioma == curso["idioma"] and nivel == curso["nivel"]:
            return False
    return True

#Verifica as informações e cadastra o curso se estiverem corretas
def cadastrar_curso(idioma, nivel, carga_horaria, preco):

    #Verificar carga horaria
    try:
        carga_horaria = int(carga_horaria)
    except ValueError:
        return "carga_invalida"
    if carga_horaria <= 0:
        return "carga_invalida"

    #Verificar preço
    try:
        preco = float(preco)
    except ValueError:
        return "preco_invalido"
     
    if preco <= 0 or round(preco, 2) != preco:
        return "preco_invalido"
    
    #Verifica se o curso ja existe e atualiza os dados
    if verificar_curso(idioma, nivel):
        novo_id = max([curso["id"] for curso in cursos],
                          default= 0) + 1
        
        novo_curso = {"id": novo_id,
          "idioma": idioma,
          "nivel": nivel,
          "carga_horaria": carga_horaria,
          "preco": preco
          }
        cursos.append(novo_curso)
        return "sucesso"
    else:
        return "duplicado"
    
#Verifica e edita as novas informações do curso
def editar_curso(id_curso, nova_carga_horaria, novo_preco):
    for item in cursos:
        if item["id"] == id_curso:
            #Verificar carga horaria
            try:
                carga_horaria = int(nova_carga_horaria)
            except ValueError:
                return "carga_invalida"
            
            if carga_horaria <= 0:
                return "carga_invalida"

            #Verificar preço
            try:
                preco = float(novo_preco)
            except ValueError:
                return "preco_invalido"
                 
            if preco <= 0 or round(preco, 2) != preco:
                return "preco_invalido"
            
            #Atualizar os dados do curso
            item["carga_horaria"] = carga_horaria
            item["preco"] = preco

            return "sucesso"

#Verifica qual é o curso e exclui
def excluir_curso(id_curso):
    for item in cursos:
        if item["id"] == id_curso:
            cursos.remove(item)
            return "sucesso"
    else:
        return "falha"