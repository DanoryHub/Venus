FROM python:3.7-alpine

ARG requirements=requirements.txt

WORKDIR app/

COPY backend/project/requirements ./requirements

RUN pip install --upgrade pip==19.1.1 \
    && pip install --no-cache-dir -r requirements/$requirements

COPY backend/project .