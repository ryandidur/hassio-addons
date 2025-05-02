# Dockerfile for UniFi Captive Portal Add-on

# Use a lightweight Python image as the base
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy application files
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose port 80 for the web server
EXPOSE 80

# Start the application
CMD ["python", "app.py"]