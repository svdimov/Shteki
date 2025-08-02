FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Add this block BEFORE pip install if you use Pillow, psycopg2, or anything needing compilation!
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    libpq-dev \
    python3-dev \
    libjpeg-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

#RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "Shteki.wsgi:application", "--bind", "0.0.0.0:8000", "--workers=4"]
