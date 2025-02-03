# Python 3.9 slim image as base
FROM python:3.9-slim

# Setting working directory
WORKDIR /app

# Setting essential environment variables
ENV PYTHONUNBUFFERED=1

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY . .

#directories
RUN mkdir -p templates assets

# Expose the port
EXPOSE 8000

# run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]