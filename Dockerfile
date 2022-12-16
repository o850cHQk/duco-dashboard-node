# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY Duco-Dash-Worker.py



RUN echo '[Duco-Dash]' > Settings.cfg
RUN echo 'api = $API' >> Settings.cfg
RUN echo 'url = $URL' >> Settings.cfg
RUN echo 'debug = n' >> Settings.cfg

CMD [ "cat", "Settings.cfg" ]