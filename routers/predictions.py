from fastapi import Body, APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from controllers.predictions import PREDICTIONS, read_prediction


router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    predictions = PREDICTIONS

    return templates.TemplateResponse(
        "home.html", {"request": request, "predictions": predictions}
    )


@router.get("/add-prediction", response_class=HTMLResponse)
async def add_new_prediction(request: Request):

    return templates.TemplateResponse("add-prediction.html", {"request": request})


@router.get("/edit-prediction/{prediction_id}", response_class=HTMLResponse)
async def edit_prediction(request: Request, prediction_id: int):

    prediction = read_prediction(prediction_id)

    return templates.TemplateResponse(
        "edit-prediction.html", {"request": request, "prediction": prediction}
    )


@router.get("/predictions")
async def read_all_predictions():
    return PREDICTIONS


@router.get("/prediction/{prediction_id}")
async def read_prediction(prediction_id: str):
    return read_prediction(prediction_id)


@router.get("/predictions/")
async def read_type_by_query(type: str):
    predictions_to_return = []
    for prediction in PREDICTIONS:
        if prediction.get("type").casefold() == type.casefold():
            predictions_to_return.append(prediction)
    return predictions_to_return


# Get all predictions from a specific city using path or query parameters
@router.get("/predictions/byCity/")
async def read_predictions_by_city_path(author: str):
    predictions_to_return = []
    for prediction in PREDICTIONS:
        if prediction.get("author").casefold() == author.casefold():
            predictions_to_return.append(prediction)

    return predictions_to_return


@router.get("/predictions/{prediction_city}/")
async def read_prediction_city_by_query(prediction_city: str, type: str):
    predictions_to_return = []
    for prediction in PREDICTIONS:
        if (
            prediction.get("city").casefold() == prediction_city.casefold()
            and prediction.get("type").casefold() == prediction.casefold()
        ):
            predictions_to_return.append(prediction)

    return predictions_to_return


@router.post("/predictions/create_prediction")
async def create_prediction(new_prediction=Body()):
    PREDICTIONS.append(new_prediction)


@router.put("/predictions/update_prediction")
async def update_prediction(updated_prediction=Body()):
    for i in range(len(PREDICTIONS)):
        if (
            PREDICTIONS[i].get("id").casefold()
            == updated_prediction.get("id").casefold()
        ):
            PREDICTIONS[i] = updated_prediction


@router.delete("/predictions/delete_prediction/{prediction_id}")
async def delete_book(prediction_id: str):
    for i in range(len(PREDICTIONS)):
        if PREDICTIONS[i].get("id").casefold() == prediction_id.casefold():
            PREDICTIONS.pop(i)
            break
