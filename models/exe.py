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
    if write:file =open("data.txt",'w',encoding="utf-8")
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

def q4():
    # solicitar ano, sigla de ano, cargo, IdDaeleiçao
    # AnoInput = input(">> qual é o ano que deseja pesquisar dados da eleições?\n")
    # TipoEleição = input(">> qual é tipo da eleição?\n")
    # CargoEletivo = input(">> qual é o cargo?\n")

    #!! SUGERIR ESCOLHER ANO APENAS NA PROXIMA QUESTAO POIS PRECISA ACESSAR OUTRO BANCO PARA PEGAR O CODIGO DA ELEIÇÃO DO ANO
    while True:
        try:
            #inputin = input(">> ")
            listadecandidatos = list()
            cargo   =  "c"+listcodigosdecargo["CodigoPresidente"]
            tipo1   =  "br-" + cargo + urlq4Final
            #tipo2   =  "rn"+"-"+cargo+urlq4Final
            url = urlq4+tipo1


            data    = requests.get(url).json()
            for linha in data:
                for linhasub in linha:
                    #print(linha,data[linha])
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
