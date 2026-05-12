from fastapi import FastAPI
from app.schemas import HeartData, PredictionResponse
from app.model_loader import model
import pandas as pd

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Heart Disease Prediction API"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/info")
def info():
    return {
        "model": "RandomForestClassifier",
        "features": [
            "age", "sex", "cp", "trestbps",
            "chol", "fbs", "restecg", "thalach",
            "exang", "oldpeak", "slope", "ca", "thal"
        ]
    }


@app.post("/predict", response_model=PredictionResponse)
def predict(data: HeartData):

    input_data = pd.DataFrame([data.dict()])

    prediction = model.predict(input_data)[0]

    return PredictionResponse(
        heart_disease=bool(prediction)
    )