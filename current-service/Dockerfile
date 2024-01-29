FROM python:3.12-slim

WORKDIR /app

ADD requirements.txt /app/

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean

RUN pip install -r /app/requirements.txt \
    && rm -rf /root/.cache/pip

COPY . /app/

RUN cd app/
RUN uvicorn main:app --reload