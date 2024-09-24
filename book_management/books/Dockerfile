LABEL authors="galetka"

FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y build-essential libpq-dev

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

ENV DJANGO_SETTINGS_MODULE=book_management.settings
ENV PYTHONUNBUFFERED 1

EXPOSE 8000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "book_management.wsgi:application"]
