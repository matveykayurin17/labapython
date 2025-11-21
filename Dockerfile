FROM python:3.11-slim

WORKDIR /app

# Копируем зависимости
COPY requirements.txt ./

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код
COPY src/ ./src/
COPY tests/ ./tests/
COPY pyproject.toml ./
COPY README.md ./

# Устанавливаем рабочую директорию
WORKDIR /app

# Запускаем main.py из папки src
CMD ["python", "src/main.py"]