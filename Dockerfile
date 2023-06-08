FROM python:3.9-slim

RUN apt-get update -y && apt-get install -y gettext  \
    build-essential  \
    libssl-dev  \
    git  \
    python3-dev  \
    gcc  \
    libpq-dev \
    libffi-dev

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY . /app
WORKDIR /app

EXPOSE 8000

ENV PYTHONUNBUFFERED 1

ENTRYPOINT ["/bin/bash", "/app/runserver.sh"]