FROM python:3.11-slim

WORKDIR /app/src

COPY src/ ./
COPY requirements.txt ../

RUN pip install --no-cache-dir -r ../requirements.txt

CMD ["python", "main.py"]