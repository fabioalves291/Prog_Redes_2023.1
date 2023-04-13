from models.default import url1a3,urlq4
import requests
from models.exe import q1,q2,q3,q4


def main():
    data = requests.get(urlq4).json()
    q4(data=data)
    input()

if __name__== "__main__":
    main()
