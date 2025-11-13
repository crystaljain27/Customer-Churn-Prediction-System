🧠 Customer Churn Prediction System
An end-to-end Machine Learning + FastAPI + Streamlit application built by Crystal Jain.

Predicts customer churn using a production-ready ML pipeline, scalable backend API, and a clean interactive frontend UI.

🚀 Live Demo
Frontend (Streamlit App):
https://customer-churn-prediction-system-crgcyc4xjy3aurhhwjzgta.streamlit.app/

Backend API (FastAPI on Render):
https://customer-churn-prediction-system-j4zm.onrender.com/docs

🧩 Overview
Customer churn is a major challenge for telecom and subscription-based companies.
This project provides a complete ML-driven solution capable of:

Predicting customer churn

Handling real-time and batch predictions

Serving predictions through FastAPI

Offering a user-friendly Streamlit interface

Running fully online using Render + Streamlit Cloud

✨ Key Features
Machine Learning

XGBoost-based classification model

Preprocessing pipeline (encoding, scaling)

Model artifact storage

Feature importance analysis

FastAPI Backend

/predict – Single prediction endpoint

/batch/predict – CSV batch prediction endpoint

Automatic Swagger docs

Pydantic validation

Modular API structure

Streamlit Frontend

Clean UI for end-users

Real-time prediction form

Batch CSV uploader

Displays output probability & class label

Deployment Ready

Docker containerization

Render hosting (backend)

Streamlit Cloud hosting (frontend)

Clean logs and error handling

🧱 Tech Stack
Machine Learning: XGBoost, Pandas, NumPy

Backend: FastAPI, Uvicorn

Frontend: Streamlit

Deployment: Render, GitHub

🏗️ Architecture
text
               ┌────────────────────┐
               │   Streamlit UI     │
               │   (Frontend)       │
               └─────────┬──────────┘
                        │ REST API Call
                        ▼
        ┌─────────────────────────────────┐
        │           FastAPI               │
        │      (Backend Service)          │
        ├─────────────────────────────────┤
        │ Preprocessing  | Model Loader   │
        │ Feature Scaling| XGBoost Model  │
        └─────────────────┬───────────────┘
                          │
                          ▼
               ┌───────────────────┐
               │  ML Artifacts     │
               │  encoders.pkl     │
               │  scaler.pkl       │
               │  xgboost.pkl      │
               └───────────────────┘
📂 Project Structure
text
Customer-Churn-Prediction-System/
│
├── backend/
│   ├── api/routes.py
│   ├── core/config.py
│   ├── core/model_loader.py
│   ├── services/preprocessing.py
│   ├── services/prediction.py
│   └── main.py
│
├── frontend/
│   └── app.py
│
├── models/
│   ├── scaler.pkl
│   ├── label_encoders.pkl
│   ├── feature_names.pkl
│   ├── model_metadata.pkl
│   └── xgboost_model.pkl
│
├── data/
│   └── IT_customer_churn.csv
│
├── requirements.txt
├── Dockerfile
├── README.md
└── uv.lock
📡 API Endpoints
Health Check
/ – Returns API status (200 OK)

Single Prediction
POST /predict

Accepts JSON body with customer features.

Returns churn probability & label.

Request Example

json
{
  "gender": "Male",
  "SeniorCitizen": 0,
  "Partner": "Yes",
  "Dependents": "No",
  "tenure": 12,
  "PhoneService": "Yes",
  "InternetService": "Fiber optic",
  "Contract": "Month-to-month",
  "PaymentMethod": "Electronic check",
  "MonthlyCharges": 70.5,
  "TotalCharges": 840.3
}
Batch Prediction
POST /batch/predict

Uploads a CSV, returns predictions for batch.

📘 Dataset
The model uses a telecom customer churn dataset containing features such as:

Demographics (Gender, SeniorCitizen, etc.)

Contract details

Billing information

Internet & phone services

Usage behavior

🛠️ Run Locally
Clone the repo

text
git clone https://github.com/crystaljain27/Customer-Churn-Prediction-System.git
Start backend

text
cd backend
uvicorn main:app --reload
Start frontend

text
streamlit run frontend/app.py
👤 Author
Built with ❤️ by Crystal Jain
GitHub: https://github.com/crystaljain27
LinkedIn: https://www.linkedin.com/in/crystal-jain-b10025264

⭐ Support
If you find this project useful, please ⭐ star the repository!