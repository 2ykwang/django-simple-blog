FROM python:3.10.9-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV \
    # python
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    # poetry
    POETRY_VERSION=1.3.1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry'

WORKDIR /server
 
COPY . /server

ENV PORT 8000

# 의존성 설치
RUN pip install "poetry==$POETRY_VERSION"
RUN poetry install --no-interaction --no-ansi