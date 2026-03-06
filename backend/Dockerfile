FROM python:3.14.3-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . .

RUN chmod +x entrypoint.sh

CMD ["./backend/entrypoint.sh"]
