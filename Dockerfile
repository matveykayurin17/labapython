# Используем официальный Python образ
FROM python:3.12-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости сначала для кэширования
COPY requirements.txt .
COPY uv.lock .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . .

# Устанавливаем рабочую директорию для src
WORKDIR /app/labapython/src

# Запускаем main.py
CMD ["python", "main.py"]