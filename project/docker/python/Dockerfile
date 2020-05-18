FROM python:3.6-alpine

WORKDIR /apps/simbank

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip
COPY ./simbank/requirements.txt /apps/simbank/requirements.txt
RUN pip install -r requirements.txt

COPY ./simbank /apps/simbank

ENTRYPOINT ["/apps/simbank/entrypoint.sh"]

