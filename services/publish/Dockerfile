FROM python:alpine3.17

ARG USER=worker
RUN adduser -D $USER
USER $USER

WORKDIR /src

COPY requirements.txt /src/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt

COPY main.py /src/
COPY ./app /src/app
