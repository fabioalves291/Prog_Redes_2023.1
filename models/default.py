import requests

def menu():
    
    print(50*"#")
    print("Escolha a Questão")
    print("""
1 - para Q1-Listar campus da Ifrn
2 - para Q2-Listar campus e alunos
3 - para Q3-Escrever o resultado da Q2
4 - para Q4-Tratar dados e apresentar das eleiçoes""")
    print(50*"#")
    alternativa =   int(input(">> "))
    return alternativa

def request(url):
    dados_retorno = requests.get(url).json()
    return dados_retorno

url1a3      = "https://dados.ifrn.edu.br/dataset/d5adda48-f65b-4ef8-9996-1ee2c445e7c0/resource/00efe66e-3615-4d87-8706-f68d52d801d7/download/dados_extraidos_recursos_alunos-da-instituicao.json"
urlCq4      = "https://resultados.tse.jus.br/oficial/ele2022/544/config/ele-c.json"
urlq4Def    = "https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json"
def urlq4(ano,codigo3digpasta,abrangencia,cargo):
    urlq4 = rf'https://resultados.tse.jus.br/oficial/ele{ano}/{codigo3digpasta}/dados-simplificados/br/{abrangencia}-c{cargo}-e000{codigo3digpasta}-r.json'
    return urlq4

    #documentação https://www.tse.jus.br/eleicoes/eleicoes-2022/interessados-na-divulgacao-de-resultados-2022
CodigodeEleição     = {
"PrimeiroTurnoFederal"  :   "544",
"PrimeiroTurnoEstadual" :   "546",
"SegundoTurnoFederal"   :   "545",
"SegundoTurnoEstadual"  :   "547",
    }
listcodigosdecargo  =   {
"CodigoPresidente" : "0001",
"CodigoGovernador" : "0003",
"CodigoSenador"    : "0005",
"CodigoDepFedera"  : "0006",
"CodigoDepEstadua" : "0007",
"CodigoDepDistria" : "0008",
"CodigoPrefeito"   : "0011",
"CodigoVereador"   : "0013",
    }
listadeUF=(
"ro","ac","am","rr","pa","ap","to","ma"
"pi","ce","rn","pb","pe","al","se","ba"
"mg","rj","sp","pr","sc","rs","ms","mt"
"go","df"
)

hrefData="data/data.txt"

