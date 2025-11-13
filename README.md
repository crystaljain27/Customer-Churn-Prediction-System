# 🧠 Customer Churn Prediction System
An end-to-end Customer Churn Prediction System built with Machine Learning, FastAPI, and Streamlit, developed by Crystal Jain.

This project delivers a complete production-ready pipeline capable of:

🔍 Analyzing customer behavior patterns
🔮 Predicting churn probability for telecom customers
⚡ Serving real-time predictions through a high-performance FastAPI backend
🧠 Batch processing thousands of customer records at once
🎨 Providing an elegant, user-friendly Streamlit web interface
🧱 Ensuring modular, scalable, and maintainable architecture

The system integrates data preprocessing, feature engineering, model management, and interactive visualization, making it suitable for enterprise use cases, academic projects, and portfolio demonstrations.

---

## 🚀 Live Demo

### 🔹 Frontend (Streamlit App)
https://customer-churn-prediction-system-crgcyc4xjy3aurhhwjzgta.streamlit.app/

### 🔹 Backend API (FastAPI on Render)
https://customer-churn-prediction-system-j4zm.onrender.com/docs

---

## 🧩 Overview
Customer churn is a major challenge for telecom and subscription-based companies.  
This project provides a complete ML-driven solution capable of:

- ✔️ Predicting customer churn  
- ✔️ Handling real-time & batch predictions  
- ✔️ Serving predictions through FastAPI  
- ✔️ User-friendly Streamlit interface  
- ✔️ Fully deployed using Render + Streamlit Cloud  

---

## ✨ Key Features

### 🔹 Machine Learning
- XGBoost classification model  
- Full preprocessing pipeline  
- Label encoding  
- Scaling  
- Model artifacts stored for production  

### 🔹 FastAPI Backend
- `/predict` → Single prediction  
- `/batch/predict` → CSV batch prediction  
- Auto-generated API docs  
- Pydantic-based validation  
- Clean modular architecture  

### 🔹 Streamlit Frontend
- Clean UI  
- Real-time churn prediction  
- Batch CSV upload  
- Shows probability + final label  

### 🔹 Deployment Ready
- Docker support  
- Render backend hosting  
- Streamlit Cloud frontend hosting  

---

## 🧱 Tech Stack

### **Machine Learning:**  
XGBoost, Pandas, NumPy  

### **Backend:**  
FastAPI, Uvicorn  

### **Frontend:**  
Streamlit  

### **Deployment:**  
Render, Streamlit Cloud, GitHub  

---

## 🏗️ Architecture

```
               ┌────────────────────┐
               │   Streamlit UI     │
               │   (Frontend)       │
               └─────────┬──────────┘
                        │ REST API
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
```

---

## 📂 Project Structure

```
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
```

---

## 📡 API Endpoints

### 🔹 Health Check
`GET /` → Returns API status

### 🔹 Single Prediction  
`POST /predict`

**Example Request:**
```json
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
```

### 🔹 Batch Prediction  
`POST /batch/predict`

Upload a CSV → Returns churn predictions.

---

## 📘 Dataset
Dataset includes:

- Demographics  
- Contract details  
- Billing  
- Internet & phone services  
- Usage behavior  

---

## 🛠️ Run Locally

### 1️⃣ Clone the repo
```
git clone https://github.com/crystaljain27/Customer-Churn-Prediction-System.git
```

### 2️⃣ Start backend
```
cd backend
uvicorn main:app --reload
```

### 3️⃣ Start frontend
```
streamlit run frontend/app.py
```

---

## 👤 Author
Built by **Crystal Jain**  

- GitHub: https://github.com/crystaljain27  
- LinkedIn: https://www.linkedin.com/in/crystal-jain-b10025264  

---

## ⭐ Support
If you like this project, please ⭐ star the repository!
