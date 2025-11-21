FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Добавляем папку src в PYTHONPATH
ENV PYTHONPATH="/app/src:${PYTHONPATH}"

CMD ["python", "src/main.py"]