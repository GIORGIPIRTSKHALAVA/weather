# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy all files from the current directory to the working directory in the container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir requests  # Add other dependencies if needed

EXPOSE 8080

# Command to run the backend server
CMD ["python", "backend/weather.py", "backend/test_weather"]
