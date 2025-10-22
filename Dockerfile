# Use the official Python base image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory inside the container
WORKDIR /app

# Copy your local code to the container
COPY . /app

# (Optional) Install Python dependencies if you have requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Default command (you can override this in docker-compose or CLI)
CMD ["python", "run.py"]
