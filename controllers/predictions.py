from fastapi import HTTPException, Request
from jose import JWTError

PREDICTIONS = [
    {"id": "1", "type": "two_bedroom", "city": "toronto", "prediction": "2400", "complete": False},
    {"id": "2", "type": "room", "city": "mississauga", "prediction": "1000", "complete": False},
    {"id": "3", "type": "room", "city": "brampton", "prediction": "1500", "complete": False},
    {"id": "4", "type": "studio", "city": "scarborough", "prediction": "1800", "complete": False},
    {"id": "5", "type": "one_bedroom", "city": "toronto", "prediction": "2200", "complete": False},
]

    

async def read_prediction(prediction_id: str):
    try:
        for prediction in PREDICTIONS:
            if prediction.get("id").casefold() == prediction_id.casefold():
                return prediction
    except JWTError:
        raise HTTPException(status_code=404, detail="Not found")