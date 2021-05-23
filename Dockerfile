FROM python:3.7
LABEL maintainer="daniel@nibon.se"

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        gettext && \
    rm -rf /var/lib/apt/lists/*

ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV dev

COPY ./requirements.txt /code/requirements.txt
RUN pip install -U pip
RUN pip install -r /code/requirements.txt

COPY . /code/
WORKDIR /code/

CMD bash
