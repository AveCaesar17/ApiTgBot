FROM python:3.8


WORKDIR /app
COPY ./ ./
RUN apt update 
RUN apt install -y supervisor 
RUN apt install -y python3
RUN apt install -y python3-pip

RUN pip3 install --no-cache-dir flask
RUN pip3 install aiogram 
RUN pip3 install requests


#RUN pip3 install --no-cache-dir prometheus_flask_exporter





ENTRYPOINT ["python3", "api.py"]
