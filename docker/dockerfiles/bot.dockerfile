FROM python:3.8


WORKDIR /app
COPY ./ ./

RUN pip3 install --no-cache-dir flask
RUN pip3 install aiogram 
RUN pip3 install requests


#RUN pip3 install --no-cache-dir prometheus_flask_exporter




ENTRYPOINT ["python3","bot.py"]
