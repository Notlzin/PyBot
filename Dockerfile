# Dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

COPY .env ./

RUN apt-get update && apt-get install -y build-essential

RUN python -m nltk.downloader punkt wordnet

RUN gcc text_analyzer.c -o text_analyzer.exe

CMD ["python", "main.py"]
