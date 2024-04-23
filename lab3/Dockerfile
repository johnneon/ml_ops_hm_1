# Base image
FROM alpine

# Install python
RUN apk add python3

# Set working dir up
WORKDIR /app

# Copy project files
COPY . /app

# Install python libs
RUN pip install -r requirements.txt

# Prepare model
CMD python model.py

# Run application
CMD uvicorn src.main:app --host 0.0.0.0 --port 8000
