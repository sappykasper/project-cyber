FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
COPY .env .env
COPY main.py main.py

RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["python", "main.py"]