FROM python:3

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir matplotlib && \
    pip install --no-cache-dir requests
