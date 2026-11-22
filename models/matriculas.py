from models.alunos import alunos
from models.cursos import cursos

#Lista de matriculas
matriculas = [{"id": 1,
               "id_aluno": 1,
               "id_curso": 1,
               "status": "Ativa"
               },
               {"id": 2,
               "id_aluno": 2,
               "id_curso": 3,
               "status": "Cancelada"
               }]

#Cadastra a matricula
def cadastrar_matricula(id_aluno,id_curso):
    #Variavel controle
    aluno_existe = False
    curso_existe = False

    #Verifica se o aluno existe
    for aluno in alunos:
        if aluno["id"] == id_aluno:
            aluno_existe = True

    #Verifica se o curso existe
    for curso in cursos:
        if curso["id"] == id_curso:
            curso_existe = True

    #Retorna inexistente se não existir
    if not aluno_existe or not curso_existe:
        return "inexistente"

    #Busca o curso no qual se deseja fazer a matricula
    curso_novo = None
    
    for curso in cursos:
        if curso["id"] == id_curso:
            curso_novo = curso
            break

    #Verifica se o aluno ja está matriculado no curso e se está ativa
    for item in matriculas:
        if item["id_aluno"] == id_aluno and item["id_curso"] == id_curso and item["status"] == "Ativa":
            return "duplicado"
    
        #Verifica se o curso matriculado é o mesmo que o que se deseja matricular
        if item["id_aluno"] == id_aluno and item["status"] == "Ativa":

            curso_matriculado = None

            for curso in cursos:
                if curso["id"] == item["id_curso"]:
                    curso_matriculado = curso
                    break

            if curso_matriculado is not None:
                if curso_matriculado["idioma"] == curso_novo["idioma"]:
                    return "nivel existente" 
 
    #Adiciona os dados a lista matriculas
    matriculas.append({"id": len(matriculas) + 1,
               "id_aluno": id_aluno,
               "id_curso": id_curso,
               "status": "Ativa"
               })
    return "sucesso"

#Verifica o status da matricula e cancela se estiver ativa
def cancelar_matricula(id_matricula):
    for item in matriculas:
        #Procura a matricula pelo id
        if item["id"] == id_matricula:
            #Verifica se já está cancelada
            if item["status"] == "Cancelada":
                return "ja_cancelada"
            #Se estiver ativa muda para cancelada
            item["status"] = "Cancelada"
            return "sucesso"
    #Retorna inexistente caso não ache
    return "inexistente"

def buscar_matriculas(pesquisa):
    #Lista vazia que guarda os resultados
    resultados = []

    for item in matriculas:
        #Procura o aluno correspondente ao id de cada matricula
        for aluno in alunos:
            if aluno["id"] == item["id_aluno"]:
                #Compara o texto pesquisado com o nome do aluno
                if pesquisa.lower() in aluno["nome"].lower():
                    #Adiciona a lista caso encontre
                    resultados.append(item)
                    break
    return resultados