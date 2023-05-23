import requests
from models.default import url1a3,urlq4,urlCq4,menu,request
from models.exe import q1,q2,q3,q4,q5,q6


def main():
    
    alternativa = menu()
    if 1 or 2 or 3:
        data = request(url1a3)
    match alternativa:
        case 1:
            q1(data=data)
        case 2:
            q2(data=data)
        case 3:
            q3(data)
        case 4:
            q4()
        case 5:
            q5()
        case 6:
            q6()
            


if __name__== "__main__":
    main()
