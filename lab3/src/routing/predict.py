from fastapi import APIRouter
from src.schemas.predict import PredictProps
from src.services.predict import predict as predict_func

router = APIRouter(prefix="/predict")


@router.post("")
async def predict(props: PredictProps):
    """Predict route"""

    result = predict_func([[props.sepal_length, props.sepal_width, props.petal_length, props.petal_width]])
    return result
