# Use a smaller Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Install system dependencies (only what's needed)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev gcc && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy requirements file first for better caching
COPY requirements.txt .

# Install dependencies in a virtual environment for isolation
RUN python -m venv venv && \
    . venv/bin/activate && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project
COPY . .

# Expose port
EXPOSE 8000

# Use virtual environment and start Django
CMD ["/bin/sh", "-c", ". venv/bin/activate && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
