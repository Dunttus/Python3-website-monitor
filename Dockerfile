FROM python:3.12.0b3-slim

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir requests
