FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN apt-get update && apt-get install -y postgresql-client
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x ./entrypoint.sh

EXPOSE 5002
EXPOSE 50054

ENTRYPOINT ["./entrypoint.sh"]

CMD ["python", "app.py"]
