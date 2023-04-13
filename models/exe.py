
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
    if write:file =open("data.txt",'w')
    if arg: sigla_campus = input('Informe a Sigla do Campus: ').upper()
    if sigla_campus in campi or write:
        filtro = lambda c: c['campus'] == sigla_campus
        alunos = list(filter(filtro, data))
        cursos = set(map(lambda c: c['curso'], alunos))
        for curso in cursos:
            filtro = lambda c: c['curso'] == curso
            alunos_curso = list(filter(filtro, alunos))
            qt_alunos = len(alunos_curso)
            dataline = f'Curso {curso}: {qt_alunos} Alunos'
            if write:file.write(dataline+"\n");print("escrevendo")
            if arg: print(dataline)
    else:
        if arg: print('Não existe esse campus...')
   
   
        

def q3(data):
    # Exercício: Gerar arquivo com os dados da questão 02, 
    # cada curso em uma linha, separando o nome do curso da
    # quantidade de alunos por
    cursos = q2(arg=False,data=data,write=True)
    input(">> finalizado \n>>")

def q4(data):
    # solicitar ano, sigla de ano, cargo, IdDaeleiçao
    for linha in data:
        input(linha)
        for datalinha in data[linha]:
            input(datalinha);print(type(datalinha))
    pass
