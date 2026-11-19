cursos = [{"id": 1,
          "idioma": "Inglês",
          "nivel": "Básico",
          "carga_horaria": 40,
          "preco": 150.00
          }]

def verificar_curso(idioma, nivel):
    for curso in cursos:
        if idioma == curso["idioma"] and nivel == curso["nivel"]:
            return False
    return True

def cadastrar_curso(idioma, nivel, carga_horaria, preco):
    try:
        carga_horaria = int(carga_horaria)
    except ValueError:
        return "carga_invalida"
    if carga_horaria <= 0:
        return "carga_invalida"

    try:
        preco = float(preco)
    except ValueError:
        return "preco_invalido"
     
    if preco <= 0 or round(preco, 2) != preco:
        return "preco_invalido"

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

def editar_curso(id_curso, nova_carga_horaria, novo_preco):
    for item in cursos:
        if item["id"] == id_curso:
            try:
                carga_horaria = int(nova_carga_horaria)
            except ValueError:
                return "carga_invalida"
            if carga_horaria <= 0:
                return "carga_invalida"
            
            try:
                preco = float(preco)
            except ValueError:
                return "preco_invalido"
                 
            if preco <= 0 or round(preco, 2) != preco:
                return "preco_invalido"