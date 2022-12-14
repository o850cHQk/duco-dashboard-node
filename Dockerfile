FROM       python:3.8-slim-buster
COPY       . /app
WORKDIR    /app
RUN        pip3 install -r requirements.txt
ENV        SHELL=/bin/bash

ENTRYPOINT ["/bin/bash", "/app/start.sh"]