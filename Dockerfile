FROM python:3.12-alpine

COPY . /app
WORKDIR /app
RUN pip install --no-cache-dir --no-deps -r requirements.txt
CMD uvicorn main:app --host 0.0.0.0 --port 8000