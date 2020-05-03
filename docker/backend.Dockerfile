FROM python:3.7-alpine

ARG requirements=requirements.txt

WORKDIR app/

COPY backend/project .

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements/$requirements
