FROM python:3.11-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# COPY .env .env
COPY main.py main.py

EXPOSE 5000

CMD ["python", "main.py"]