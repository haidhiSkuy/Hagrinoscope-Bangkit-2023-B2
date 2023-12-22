from PIL import Image
from io import BytesIO
import firebase_module
from typing import List
from ml_model import model
from fastapi import FastAPI, UploadFile

app = FastAPI()


def load_image(data):
    return Image.open(BytesIO(data))


@app.get("/")
def hello():
    return {"hello": "world"}


@app.post("/predict/")
async def upload_file(anjay: List[UploadFile]):
    contents = [await img.read() for img in anjay]
    fruit, soil = load_image(contents[0]), load_image(contents[1])

    fruit_prediction = model.fruit_predict(fruit)
    soil_prediction = model.soil_predict(soil)

    fruit_recommendation, soil_recommendation = firebase_module.give_recommendation(fruit_prediction, soil_prediction)

    return {
        "fruit": fruit_prediction,
        "soil": soil_prediction,
        "fruit_recommendation": fruit_recommendation,
        "soil_recommendation": soil_recommendation
    }
