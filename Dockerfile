FROM python:3.12-slim

# Evita criar .pyc e buffer no log
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Instala dependências do sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copia requirements primeiro (cache de build)
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copia o restante do projeto
COPY . .

EXPOSE 8000

# Comando que roda ao subir o container
CMD sh -c "python manage.py makemigrations && \
           python manage.py migrate && \
           python manage.py runserver 0.0.0.0:8000"