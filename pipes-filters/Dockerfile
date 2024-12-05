FROM python:alpine3.17
WORKDIR /src

ARG USER=worker
RUN adduser -D $USER
USER $USER

COPY requirements.txt /src/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt

COPY main.py /src/
COPY ./app /src/app
