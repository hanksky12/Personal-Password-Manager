FROM --platform=$TARGETPLATFORM python:3.11-slim AS builder


WORKDIR /app
COPY requirements.txt /app
COPY loop.py /app
RUN  apt-get update && \
     apt-get install -y vim && \
     pip3 install -r requirements.txt


CMD ["python3", "loop.py"]

LABEL image_name="password-manager"
LABEL version="1.0"