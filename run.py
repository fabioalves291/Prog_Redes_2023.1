from models.default import url
import requests
from models.exe import q1,q2,q3


def main():
    data = requests.get(url).json()
    q3(data=data)
    input

if __name__== "__main__":
    main()
