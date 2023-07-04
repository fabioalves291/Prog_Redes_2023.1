import requests

api_key =   ["6392875575:AAHBcQqDbaHLNXsEUpb1WUfCsFwWsQKRlZA"]
url_req    =   f"https://api.telegram.org/bot{api_key}"
requecição = requests.get(url_req+"/getUpdates")
requisição = requests.get(url_req)
print(requisição.statuscode)
retorno = requisição.json()
print(requests.json())
msg = input("digite algo")
resposta = {"chat_id":id_chat,"text":msg}
envio = requests.post(url_req+"/sendMenssage",data=resposta)
