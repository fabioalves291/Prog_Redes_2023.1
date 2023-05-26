# -*- coding: utf-8 -*-
#! bin/lib/python
import requests
from models.default import url1a3,urlq4,urlCq4,menu,request
from models.exe import q1,q2,q3,q4,q5,q6
import sys

def main():
    alternativa = menu()
    if 1 or 2 or 3:
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
    else:
        print("opção inválida")
      
      
if __name__== "__main__":
    main()
