FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app/

RUN set -e; \
    pip -q install --upgrade pip && \
    pip -q install --no-cache-dir -r requirements.txt && \
    pip check

COPY . /app/

CMD ["python","-m","main"]
