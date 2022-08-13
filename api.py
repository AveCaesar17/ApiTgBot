from flask import Flask, request
from flask import Flask, Response
#from prometheus_flask_exporter import PrometheusMetrics
app = Flask(__name__)
#metrics = PrometheusMetrics(app)
import os 
import subprocess
import requests
counter = 0
# by_path_counter = metrics.counter(
#     'by_path_counter', 'Request count by request paths',
#     labels={'path': lambda: request.path}
# )
@app.route('/getcall', methods=['POST'])
#@by_path_counter
def send():
    input_json = request.get_json(force=True) 
    name = input_json["name"]
    phone = input_json["phone"]
    chatid = []
    with open("chat_id.txt") as file:
        for item in file:
            print(item)
            chatid.append(item.replace("\n",""))
    message = "Заказан звонок на номер\n" + phone + "\n" + name
    for id in chatid:
        requests.get('https://api.telegram.org/bot{}/sendMessage'.format(os.environ.get("TG_BOT_TOKEN")), params=dict(
                    chat_id=id,
                    text=message
                    ))
    return Response(input_json, mimetype='text/plain')
#metrics.info('app_info', 'Application info', version=counter)



app.run(host='0.0.0.0',port=5000)