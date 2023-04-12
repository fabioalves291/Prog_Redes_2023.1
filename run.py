from models.default import url
import requests
from models.exe import Q2


def main():
    data = requests.get(url).json()
    Q2(True,data=data)
    input

if __name__== "__main__":
    main()