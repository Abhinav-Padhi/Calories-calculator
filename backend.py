from fastapi import FastAPI, UploadFile, File
from ultralytics import YOLO
from PIL import Image
import io

app = FastAPI()

model = YOLO("best.pt")

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image = Image.open(io.BytesIO(await file.read()))

    results = model(image)

    predictions = []

    for box in results[0].boxes:
        predictions.append({
            "class": model.names[int(box.cls)],
            "confidence": float(box.conf)
        })

    return {"predictions": predictions}