# -*- coding: utf-8 -*-
#! bin/lib/python3
import requests

from models.default import url1a3,urlq4,urlCq4,menu#,request
from models.exe import q1,q2,q3,q4,q5,q6,q7,q8
import sys

def main():
    alternativa = menu()
    if alternativa == 1 or alternativa == 2 or alternativa == 3:
        data = request(url1a3)
    #match so funcionar no python 3.10 para cima!
    #match alternativa:
    match alternativa:
        case 1:
            q1(data=data)
        case  2:
            q2(data=data)
        case  3:
            q3(data)
        case 4:
            q4()
        case  5:
            q5()
        case  6:
            q6()
        case  7:
            q7()
        case  8:
            q8()
        case _:
            print("opção inválida")
        
if __name__== "__main__":
    main()
