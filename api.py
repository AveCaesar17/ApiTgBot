from crypt import methods
from flask import Flask, request
from flask import Flask, Response
app = Flask(__name__)
import os 
import subprocess
import requests
counter = 0

@app.route('/getcall', methods=['POST'])
def send():
    input_json = request.get_json(force=True) 
    name = input_json["name"]
    phone = input_json["phone"]
    message = "Заказан звонок на номер\n{}\n{}".format(phone,name)
    print(message)
    send_message(message)
    return Response(input_json, mimetype='text/plain')

@app.route("/create", methods=['POST'])
def create(): 
    pass

def send_message(message):
    chatid = []
    with open("chat_id.txt") as file:
        for item in file:
            chatid.append(item.replace("\n",""))
    for id in chatid:
        requests.get('https://api.telegram.org/bot{}/sendMessage'.format(os.environ.get("TG_BOT_TOKEN")), params=dict(
                    chat_id=id,
                    text=message
                    ))
    return



app.run(host='0.0.0.0',port=5000)