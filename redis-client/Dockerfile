FROM python:3.9-alpine3.13

WORKDIR /app

RUN apk add curl && pip install --user --no-cache-dir flask redis

COPY redis-client.py ./

CMD [ "python", "redis-client.py" ]
