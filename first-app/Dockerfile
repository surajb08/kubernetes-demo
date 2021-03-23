FROM python:3.9-alpine3.13

RUN apk add curl && adduser -D flask-app

USER flask-app

WORKDIR /app

RUN pip install --user --no-cache-dir flask requests

COPY first-app.py ./

CMD [ "python", "first-app.py" ]