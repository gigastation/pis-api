FROM python:3
RUN apt-get update && apt-get -y install sqlite3 libsqlite3-dev
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

