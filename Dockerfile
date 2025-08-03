FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN apt-get update && apt-get install -y gcc libpq-dev
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "Shteki.wsgi:application", "--bind", "0.0.0.0:80", "--workers", "4"]
