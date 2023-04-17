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

def CasoSuportIdentifcar(abrangencia,turno):
    if abrangencia =="br" and turno == "1":
        return CodigodeEleição["PrimeiroTurnoFederal"]
    elif abrangencia =="br" and turno == "2":
        return CodigodeEleição["SegundoTurnoFederal"]
    elif not abrangencia == "br" and turno == "1":
        return CodigodeEleição["PrimeiroTurnoEstadual"]
    elif not abrangencia == "br" and turno == "2":
        return CodigodeEleição["SegundoTurnoEstadual"]

def PrintDictSubQ4(dictdata):
    for chaves in dictdata:
        print(chaves,(20 -len(chaves))*" ",dictdata[chaves])

def subQ4menu():
    abrangencia = input(">> digite o Tipo da eleição\n 1 para Federal\n 2 para Estadual\n>> ")
    if abrangencia == "2":
        abrangencia = input(">>digite a UF desejada\n>> ")
    else:abrangencia = "br"
    turno = input(">> digite o Turno \n 1 para primeiro\n 2 para segundo\n>> ")
    codigo3digpasta = CasoSuportIdentifcar(abrangencia,turno)
    ano = input(">> digite o ano da eleição\n>> ")
    map(PrintDictSubQ4(listcodigosdecargo),listcodigosdecargo)
    cargo = input(">> digite o cadigo do cargo\n>> ")
    return ano,codigo3digpasta,abrangencia,cargo

def q4():
    # solicitar ano, sigla de ano, cargo, IdDaeleiçao
    ano,codigo3digpasta,abrangencia,cargo =  subQ4menu()
    #codigo3digpasta =input("digite o codigo da eleição refente ao ano de eleição e turno...")
    print(ano,codigo3digpasta,abrangencia,cargo)
    input(urlq4(ano,codigo3digpasta,abrangencia,cargo))
    #input(urlq4Def)
    #input(urlq4(ano,codigo3digpasta,abrangencia,cargo))
    data = request(urlq4(ano,codigo3digpasta,abrangencia,cargo))
    # esquecer comentario acima... depende do ts para resolver essa funcionalidade ou criar um arquivo json suport
    while True:
        try:
            listadecandidatos = list()
            for linha in data:
                for linhasub in linha:
                    break
            CandidatosData = data["cand"]
            for candidatos in CandidatosData:
                candidatos["n"]
                listadecandidatos.append({candidatos["n"]+"_candidado":{"nome":candidatos["nm"],"partido":candidatos["cc"],"votos":candidatos["vap"],"percentual":candidatos["pvap"]}})
            for dados in listadecandidatos:
                print(dados)
            return listadecandidatos
            exit()
        finally:
            pass
    pass
    