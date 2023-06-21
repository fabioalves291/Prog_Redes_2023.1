# -*- coding: utf-8 -*-
#! bin/lib/python
#import requests
from models.default import url1a3,urlq4,urlCq4,menu,request
from models.exe import q1,q2,q3,q4,q5,q6,q7
import sys

def main():
    alternativa = menu()
    if alternativa == 1 or alternativa == 2 or alternativa == 3:
        data = request(url1a3)
    #match so funcionar no python 3.10 para cima!
    #match alternativa:
    if alternativa == 1:
        q1(data=data)
    elif alternativa == 2:
        q2(data=data)
    elif alternativa == 3:
        q3(data)
    elif alternativa == 4:
        q4()
    elif alternativa == 5:
        q5()
    elif alternativa == 6:
        q6()
    elif alternativa == 7:
        q7()
    elif alternativa == 8:
        pass
    else:
        print("opção inválida")
      
if __name__== "__main__":
    main()
