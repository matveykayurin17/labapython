FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt


ENV PYTHONPATH=/app/src

CMD ["python", "src/main.py"]