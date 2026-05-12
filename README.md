# Heart Disease Prediction API

A machine learning API built using FastAPI, Docker, and Scikit-learn for predicting heart disease.

## Project Overview

This project:

* Trains a machine learning model using the Heart Disease Dataset
* Serves predictions using FastAPI
* Dockerizes the application
* Deploys the application on Render

The goal of this assignment is to practice:

* FastAPI
* Docker
* Docker Compose
* API development
* Cloud deployment

---

# Live Deployment URL

Application URL:

```bash
https://heart-disease-api-nnw4.onrender.com
```

Swagger Documentation:

```bash
https://heart-disease-api-nnw4.onrender.com/docs
```

---

# Tech Stack

* Python
* FastAPI
* Scikit-learn
* Pandas
* Docker
* Docker Compose
* Uvicorn
* Render

---

# Project Structure

```bash
heart-disease-api/
│
├── app/
│   ├── main.py
│   ├── schemas.py
│   └── model_loader.py
│
├── model/
│   ├── train_model.py
│   └── heart_model.joblib
│
├── data/
│   └── heart.csv
│
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── README.md
└── .gitignore
```

---

# Dataset

Dataset used:

[https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset](https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset)

---

# Features Used

The model uses the following features:

* age
* sex
* cp
* trestbps
* chol
* fbs
* restecg
* thalach
* exang
* oldpeak
* slope
* ca
* thal

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone https://github.com/ghorardim/heart-disease-api
cd heart-disease-api
```

---

## 2. Create Virtual Environment

### macOS/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows

```bash
python -m venv .venv
.venv\\Scripts\\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Train the Model

Run:

```bash
python model/train_model.py
```

This generates:

```bash
model/heart_model.joblib
```

---

# Run FastAPI Locally

Run:

```bash
uvicorn app.main:app --reload
```

Open Swagger UI:

```bash
http://localhost:8000/docs
```

---

# API Endpoints

## GET /

Returns welcome message.

---

## GET /health

Checks API health status.

### Response

```json
{
  "status": "healthy"
}
```

---

## GET /info

Returns model information and feature list.

---

## POST /predict

Predicts whether heart disease is present.

### Sample Request

```json
{
  "age": 63,
  "sex": 1,
  "cp": 3,
  "trestbps": 145,
  "chol": 233,
  "fbs": 1,
  "restecg": 0,
  "thalach": 150,
  "exang": 0,
  "oldpeak": 2.3,
  "slope": 0,
  "ca": 0,
  "thal": 1
}
```

### Sample Response

```json
{
  "heart_disease": true
}
```

---

# Docker Setup

## Build Docker Image

```bash
docker compose build
```

---

## Run Docker Container

```bash
docker compose up
```

---

## Stop Docker Container

```bash
docker compose down
```

---

# Docker Commands

## View Running Containers

```bash
docker ps
```

## View Images

```bash
docker images
```

---

# Deployment

1. Push project to GitHub
2. Create Render Web Service
3. Select Docker environment
4. Connect repository
5. Deploy

---

# Author

Abdullah Al Mahmud Jabir

---

# License

Educational assignment project.