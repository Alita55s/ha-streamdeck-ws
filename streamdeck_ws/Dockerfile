FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    libusb-1.0-0 \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir streamdeck websockets

WORKDIR /app
COPY app.py /app/app.py

CMD ["python", "/app/app.py"]
