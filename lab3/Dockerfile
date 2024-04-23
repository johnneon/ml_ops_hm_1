# Base image
FROM python:3.9-slim

# Install some other stuff for building packages
# Set working dir up
WORKDIR /app

# Copy project files
COPY . /app

# Use virtual env
# Install python libs
RUN pip install -r requirements.txt

# Prepare model
RUN python src/model.py

# Run application
CMD uvicorn src.main:app --host 0.0.0.0 --port 8000
