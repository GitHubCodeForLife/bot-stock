# Use the official Python base image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
# Set timezone environment variable
ENV TZ=Asia/Bangkok
# Set working directory inside the container
WORKDIR /app

# Copy your local code to the container
COPY . /app

RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*
    
# (Optional) Install Python dependencies if you have requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Default command (you can override this in docker-compose or CLI)
# uwsgi --ini uwsgi.ini
CMD ["uwsgi ", "--ini", "uwsgi.ini"]
