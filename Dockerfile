# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY Duco-Dash-Worker.py
COPY start.sh

CMD [ "./start.sh" ]