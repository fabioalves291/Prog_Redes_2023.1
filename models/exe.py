import requests
from models.default import *

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
    if write:file =open(hrefData,'w',encoding="utf-8")
    if arg: sigla_campus = input('Informe a Sigla do Campus: ').upper()
    for sigla_campus in campi or write:
        if not sigla_campus in campi:print("nao esta lsiado campos")
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
    if write:file.close()
def q3(data):
    # Exercício: Gerar arquivo com os dados da questão 02, 
    # cada curso em uma linha, separando o nome do curso da
    # quantidade de alunos por
    cursos = q2(arg=False,data=data,write=True)
    input(">> finalizado \n>>")

def usbQ4menu():
    
    tipo = print(">> digite o Tipo da eleição\n>> -0 para federal\n -1 para estadual")
    input(">> ")
    print(">> digite o ano da eleição")
    input(">> ")
    print(">> digite o cargo\n")
    input(">> ")
    if tipo:
        print(">> digite o UF")
    input(">> ")

    return
def q4():
    # solicitar ano, sigla de ano, cargo, IdDaeleiçao
    ano,cocodigo3digpasta,abrangencia,cargo=submenu()
    input(urlq4Def)
    input(urlq4(ano="2022",codigo3digpasta="544",abrangencia="br",cargo=listcodigosdecargo["CodigoPresidente"]))
    data = request(urlq4(ano="2022",codigo3digpasta="544",abrangencia="br",cargo=listcodigosdecargo["CodigoPresidente"]))
    #!! SUGERIR ESCOLHER ANO APENAS NA PROXIMA QUESTAO POIS PRECISA ACESSAR OUTRO BANCO PARA PEGAR O CODIGO DA ELEIÇÃO DO ANO
    # esquecer comentario acima... dependo do ts para resolver essa funcionalidade ou criar um arquivo json suport
    while True:
        try:
            listadecandidatos = list()
            for linha in data:
                for linhasub in linha:
                    break
            CandidatosData = data["cand"]
            for candidatos in CandidatosData:
                candidatos["n"]
                listadecandidatos.append({candidatos["n"]+"_candidado":{"nome":candidatos["nm"],"partido":candidatos["cc"],"votos":candidatos["vap"]}})
            for dados in listadecandidatos:
                print(dados)
            return listadecandidatos
            exit()
        finally:
            pass
    pass
    