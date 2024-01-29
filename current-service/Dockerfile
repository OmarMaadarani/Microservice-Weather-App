FROM python:3.12-slim

WORKDIR /app

ADD requirements.txt .

RUN pip install -r requirements.txt \
    && rm -rf /root/.cache/pip

EXPOSE 8000

COPY . .