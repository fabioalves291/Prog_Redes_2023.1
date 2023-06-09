import requests
import socket,sys
import os
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
def auxiliardeSubQ4Menuserchdata():
    data = request(urlConfig)
    print(data)

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
    
def q5(url="https://images.shiksha.com/mediadata/images/1606913285phphjZJYb.png",printf=True): 
    url_heard   = url[:url.find("://")]
    url_resto   = url[url.find("://")+3:]
    url_auxiliar_host= len(url_heard) + 3
    url_host    = url[url_auxiliar_host : url_auxiliar_host + url_resto.find("/")]
    url_src_arquivo = url[url_auxiliar_host + len(url_host) + 1: ]
    name_arquivo_tipo = url_src_arquivo[url_src_arquivo.find(".",-len(url_src_arquivo)):]
   
    cont        = 0
    for letra in url_src_arquivo:
        cont    += 1
        if letra == '/':
            contultimabarra = cont
    name_arquivo = url_src_arquivo[contultimabarra:url_src_arquivo.find(".",-len(url_src_arquivo))]
    if url[:url.find("://")] == "https":
        host_port = 8080
    espaço = 15
    if printf:print(
    f"""
    head{(espaço-len("head"))*' '}{url_heard}
    host{(espaço-len("host"))*' '}{url_host}
    endereçoaqv{(espaço-len("endereçoaqv"))*' '}{url_src_arquivo}
    nomearq{(espaço-len("nomearq"))*' '}{name_arquivo}
    tipodearq{(espaço-len("tipodearq"))*' '}{name_arquivo_tipo}
    host_port{(espaço-len("host_port"))*' '}{host_port}""")
    
    url_request = f"GET {url_src_arquivo} HTTP/1.1/r/n HOST: {url_host}\r\n\r\n"
    sock_img    = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("criando conexão")
    print(url_heard+'://'+url_host)
    sock_img.connect((url_host, host_port))
    sock_img.sendall(url_request.encode())
    if printf:print("Baixando...")
    buffer_size = 522
    data_request= b""
    while True:
        data    = sock_img.recv((buffer_size))
        if not data: break
    sock_img.close()
    
    img_size = -1 
    tmp         = data_ret.split('\r\n'.encode())
    for line in tmp:
        if 'Content-Length:'.encode() in line:
            img_size = int(line.split()[1])
            break
    print(img_size,'tamnho')
    delimiter   = "\r\n\r\n".encode()
    position    = data_ret.find(delimiter)
    headers     = data_ret[:position]
    image       = data_ret[position+4:]
    
    file_output =   open("image.png","wb")
    file_outout.write(image)
    file_output.close()

def q6():
    host = input('\nInforme o nome do HOST ou URL do site: ')
    for port in (22,122,80,8080):
        print(port)
        server_conn = (host, port)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        try:
           sock.connect(server_conn)
        except socket.gaierror:
           print('\nErro no HOST...')
        except:
           print(sys.exc_info())
        else:
           print('\nConexão OK...')
           sock.close()
   
def q7():
    print("https://github.com/fabioalves291/server_udp")
    input()
def q8():
    print("https://github.com/fabioalves291/server_tcp")
    input()
    
