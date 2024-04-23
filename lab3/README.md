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

#### What Dockerfile does
1. Install base image (clean alpine)
2. Install python interpreter
3. Setting up working dir
4. Prepare ML model
5. Run API application