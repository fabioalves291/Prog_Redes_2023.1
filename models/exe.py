
def q1(arg=True, data=0):
    # Questão 01: Listar os campi e a sua 
    # quantidade de alunos
    campi = set(map(lambda c: c['campus'], data))
    for campus in campi:
        filtro = lambda c: c['campus'] == campus
        alunos = list(filter(filtro, data))
        qt_alunos = len(alunos)
        if arg: print(f'Campus {campus}: {qt_alunos} Alunos')
    return campi

def q2(arg=True,data=0,write=False):
    # Questão 02: Solicitar a sigla de um campus e listar os cursos do
    # campus e a quantidade de alunos de cada curso
    sigla_campus = str()
    campi = q1('',data)
    if write:file =open("data",'a+')
    if arg: sigla_campus = input('Informe a Sigla do Campus: ').upper()
    if sigla_campus in campi:
        filtro = lambda c: c['campus'] == sigla_campus
        alunos = list(filter(filtro, data))
        cursos = set(map(lambda c: c['curso'], alunos))
        for curso in cursos:
            filtro = lambda c: c['curso'] == curso
            alunos_curso = list(filter(filtro, alunos))
            qt_alunos = len(alunos_curso)
            varprint(f'Curso {curso}: {qt_alunos} Alunos')
            if write:write(dataline)
            if arg: print(varprint)
    else:
        if arg: print('Não existe esse campus...')
   
   
        

def q3(data):
    # Exercício: Gerar arquivo com os dados da questão 02, 
    # cada curso em uma linha, separando o nome do curso da
    # quantidade de alunos por
    cursos = q2(False,data,True)
    input(">> finalizado \n>>")

def Q4():
    #solicitar ano, sigla de ano, cargo, IdDaeleiçao
    pass
