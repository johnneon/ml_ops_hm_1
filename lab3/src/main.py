from fastapi import FastAPI
from src.routing.predict import router as predict_route

app = FastAPI()

app.include_router(predict_route)


@app.get("/")
async def root():
    """Base method with instructions"""

    return {
        "message": "For test iris classification, you should send POST request to the `/predict` endpoint, "
                   "with following parameters:",
        "body": {
            "sepal_length": 7.9,
            "sepal_width": 1.3,
            "petal_length": 8.1,
            "petal_width": 1.2
        }
    }
