FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Instala dependências de sistema necessárias para o OpenCV
RUN apt-get update && apt-get install -y \
    gcc \
    libglib2.0-0 \
    libglib2.0-dev \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgl1-mesa-glx \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Instala dependências Python
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

# Copia o script wait-for-postgres.sh e dá permissão
COPY wait-for-postgres.sh /app/wait-for-postgres.sh
RUN chmod +x /app/wait-for-postgres.sh

CMD ["sh", "-c", "/app/wait-for-postgres.sh db python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
