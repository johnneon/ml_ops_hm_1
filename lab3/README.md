# MLOps: Task №3

First things first **we have to go into `lab3` dir**, and then run other commands.

After fetch git repo, we need to install requirements:
```shell
cd lab3

pip install -r requirements.txt
```

## Model part

To get data, prepare and fit model with it, you need to run:
```shell
python model.py
```

This will create `model.pkl` and `data.csv` files.

## API part

To start API, run command bellow:
```shell
uvicorn src.main:app
```

This will start API server on localhost with port 8000 - `http://localhost:8000/`.

We have 2 endpoints:
1. Base - `GET /`
2. Predict - `POST /predict`

Base route returns the instructions about predict endpoint:
```json
{
  "message": "For test iris classification, you should send POST request to the `/predict` endpoint, with following parameters:",
  "body": {
    "sepal_length": 7.9,
    "sepal_width": 1.3,
    "petal_length": 8.1,
    "petal_width": 1.2
  }
}
```

Predict endpoint gets body with iris parameters and returns its class.
Example call:
```js
const request = await fetch('http://127.0.0.1:8000/predict', {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
    "sepal_length": 7.9,
    "sepal_width": 1.3,
    "petal_length": 8.1,
    "petal_width": 1.2
  })
})
const response = await request.json(); // -> { result: 'virginica' }
```

## Docker

We also have `Dockerfile` which describes docker image of our app
and `docker-compose.yaml` which contains instructions how to up our
application with docker container.

To start docker, you need to be in `lab3` dir, and run:
```shell
docker compose up
```

#### What Dockerfile does
1. Install base image (clean alpine)
2. Install python interpreter
3. Setting up working dir
4. Prepare ML model
5. Run API application

As main image I chose `python:3.9-slim`, because before I tried to
set up it with alpine and installing all dependencies took
about 15 minutes with Dockerfile:
```dockerfile
# Base image
FROM alpine
# Install python
RUN apk add --update python3 py3-pip
# Install some other stuff for building packages
RUN apk add --no-cache build-base python3-dev libffi-dev musl-dev openblas-dev
# Set working dir up
WORKDIR /app
# Copy project files
COPY . /app
# Use virtual env
RUN python3 -m venv ./venv
# Install python libs
RUN . venv/bin/activate && pip install -r requirements.txt && deactivate
# Prepare model
RUN . venv/bin/activate && python src/model.py && deactivate
# Run application
CMD . venv/bin/activate && uvicorn src.main:app --host 0.0.0.0 --port 8000
```