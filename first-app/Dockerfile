FROM python:3.9-alpine3.13

RUN adduser -D flask-app

USER flask-app

WORKDIR /app

RUN apk add curl && pip install --user --no-cache-dir flask requests

COPY first-app.py ./

CMD [ "python", "first-app.py" ]
