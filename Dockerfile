FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install pipenv

ENV PROJECT_DIR /usr/src/app

WORKDIR ${PROJECT_DIR}/src

COPY Pipfile Pipfile.lock ${PROJECT_DIR}/

COPY . .

RUN pipenv install --system --deploy