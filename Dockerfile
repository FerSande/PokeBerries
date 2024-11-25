# Etapa base para dependencias
FROM python:3.12-slim AS base

# Variables de entorno
ENV PYTHONUNBUFFERED=1 \
    ENVIRONMENT=production

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libffi-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install streamlit

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN useradd -ms /bin/bash appuser
USER appuser

EXPOSE 8000 8501

CMD uvicorn app.main:app --host 0.0.0.0 --port 8000 & streamlit run app/streamlit_app.py --server.port 8501 --server.address 0.0.0.0