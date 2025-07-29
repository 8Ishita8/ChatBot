
FROM python:3.10-slim

RUN apt-get update && \
    apt-get install -y curl git && \
    curl -fsSL https://ollama.com/install.sh | sh


ENV PATH="/root/.ollama/bin:$PATH"


RUN ollama pull mistral:7b-instruct


WORKDIR /app


COPY . /app


RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
