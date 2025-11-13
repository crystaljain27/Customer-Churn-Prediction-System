# Customer Churn Prediction API

FastAPI-based REST API for predicting customer churn using XGBoost machine learning model.

## Project Structure

```
backend/
├── main.py                 # Application entry point
├── api/                    # API routes
│   ├── __init__.py
│   └── routes.py          # Route handlers
├── core/                   # Core configuration
│   ├── __init__.py
│   ├── config.py          # Application settings
│   └── model_loader.py    # Model management
├── models/                 # Pydantic models
│   ├── __init__.py
│   ├── request.py         # Request models
│   └── response.py        # Response models
├── services/               # Business logic
│   ├── __init__.py
│   ├── preprocessing.py   # Data preprocessing
│   └── prediction.py      # Prediction service
└── README.md              # This file
```

## Features

- **Clean Architecture**: Modular design with separation of concerns
- **Single Prediction**: Predict churn for individual customers
- **Batch Prediction**: Predict churn for multiple customers at once
- **Model Information**: Get model performance metrics and metadata
- **Health Check**: Check API and model status
- **Auto Documentation**: Interactive API documentation with Swagger UI

## Setup

### 1. Train and Save the Model

First, run the Jupyter notebook `churn.ipynb` to train the model and save the artifacts. The notebook will create a `models/` directory with:
- `xgboost_model.pkl` - Trained XGBoost model
- `scaler.pkl` - StandardScaler for feature scaling
- `label_encoders.pkl` - Label encoders for categorical variables
- `feature_names.pkl` - Feature names
- `model_metadata.pkl` - Model performance metrics

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the API

From the project root directory:

```bash
cd backend
python main.py
```

Or using uvicorn directly:

```bash
# From project root
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

## API Documentation

Once the server is running, access the interactive API documentation at:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## API Endpoints

### 1. Root Endpoint
```
GET /
```
Returns basic API information and available endpoints.

**Response:**
```json
{
  "message": "Customer Churn Prediction API",
  "version": "1.0.0",
  "status": "active",
  "endpoints": {
    "POST /predict": "Single customer prediction",
    "POST /predict/batch": "Batch prediction for multiple customers",
    "GET /model/info": "Get model information",
    "GET /health": "Health check"
  }
}
```

### 2. Health Check
```
GET /health
```
Check if the API is running and model is loaded.

**Response:**
```json
{
  "status": "healthy",
  "model_loaded": true
}
```

### 3. Model Information
```
GET /model/info
```
Get information about the trained model.

**Response:**
```json
{
  "model_name": "XGBoost",
  "f1_score": 0.8632,
  "accuracy": 0.8623,
  "precision": 0.8578,
  "recall": 0.8686,
  "roc_auc": 0.9311,
  "n_features": 30,
  "training_date": "2025-10-06 14:30:00"
}
```

### 4. Single Customer Prediction
```
POST /predict
```
Predict churn for a single customer.

**Request Body:**
```json
{
  "gender": "Male",
  "SeniorCitizen": 0,
  "Partner": "Yes",
  "Dependents": "No",
  "tenure": 12,
  "PhoneService": "Yes",
  "MultipleLines": "No",
  "InternetService": "Fiber optic",
  "OnlineSecurity": "No",
  "OnlineBackup": "Yes",
  "DeviceProtection": "No",
  "TechSupport": "No",
  "StreamingTV": "Yes",
  "StreamingMovies": "Yes",
  "Contract": "Month-to-month",
  "PaperlessBilling": "Yes",
  "PaymentMethod": "Electronic check",
  "MonthlyCharges": 85.50,
  "TotalCharges": 1026.00
}
```

**Response:**
```json
{
  "churn_prediction": 1,
  "churn_probability": 0.78,
  "churn_label": "Churn",
  "risk_level": "High"
}
```

### 5. Batch Prediction
```
POST /predict/batch
```
Predict churn for multiple customers at once.

**Request Body:**
```json
{
  "customers": [
    {
      "gender": "Male",
      "SeniorCitizen": 0,
      "Partner": "Yes",
      ...
    },
    {
      "gender": "Female",
      "SeniorCitizen": 1,
      "Partner": "No",
      ...
    }
  ]
}
```

**Response:**
```json
{
  "predictions": [
    {
      "churn_prediction": 1,
      "churn_probability": 0.78,
      "churn_label": "Churn",
      "risk_level": "High"
    },
    {
      "churn_prediction": 0,
      "churn_probability": 0.23,
      "churn_label": "No Churn",
      "risk_level": "Low"
    }
  ],
  "total_customers": 2,
  "predicted_churners": 1,
  "churn_rate": 0.5
}
```

## Architecture Overview

### Core Layer
- **config.py**: Centralized configuration management
- **model_loader.py**: Singleton pattern for model artifact management

### Models Layer
- **request.py**: Input validation using Pydantic
- **response.py**: Structured response models

### Services Layer
- **preprocessing.py**: Data transformation and feature engineering
- **prediction.py**: Business logic for predictions

### API Layer
- **routes.py**: Route handlers and endpoint definitions
- **main.py**: Application initialization and middleware setup

## Risk Levels

The API categorizes churn risk into three levels:
- **Low Risk**: Churn probability < 0.3
- **Medium Risk**: Churn probability 0.3 - 0.6
- **High Risk**: Churn probability > 0.6

## Testing the API

### Using cURL

```bash
# Health check
curl http://localhost:8000/health

# Model info
curl http://localhost:8000/model/info

# Single prediction
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "gender": "Male",
    "SeniorCitizen": 0,
    "Partner": "Yes",
    "Dependents": "No",
    "tenure": 12,
    "PhoneService": "Yes",
    "MultipleLines": "No",
    "InternetService": "Fiber optic",
    "OnlineSecurity": "No",
    "OnlineBackup": "Yes",
    "DeviceProtection": "No",
    "TechSupport": "No",
    "StreamingTV": "Yes",
    "StreamingMovies": "Yes",
    "Contract": "Month-to-month",
    "PaperlessBilling": "Yes",
    "PaymentMethod": "Electronic check",
    "MonthlyCharges": 85.50,
    "TotalCharges": 1026.00
  }'
```

### Using Python

```python
import requests

# Single prediction
url = "http://localhost:8000/predict"
data = {
    "gender": "Male",
    "SeniorCitizen": 0,
    "Partner": "Yes",
    "Dependents": "No",
    "tenure": 12,
    "PhoneService": "Yes",
    "MultipleLines": "No",
    "InternetService": "Fiber optic",
    "OnlineSecurity": "No",
    "OnlineBackup": "Yes",
    "DeviceProtection": "No",
    "TechSupport": "No",
    "StreamingTV": "Yes",
    "StreamingMovies": "Yes",
    "Contract": "Month-to-month",
    "PaperlessBilling": "Yes",
    "PaymentMethod": "Electronic check",
    "MonthlyCharges": 85.50,
    "TotalCharges": 1026.00
}

response = requests.post(url, json=data)
print(response.json())
```

## Model Performance

The XGBoost model achieves the following performance metrics:
- **F1-Score**: 0.8632
- **Accuracy**: 0.8623
- **Precision**: 0.8578
- **Recall**: 0.8686
- **ROC-AUC**: 0.9311

## Features Used

The model uses 30 features including:
- Customer demographics (gender, senior citizen status, partner, dependents)
- Service information (phone, internet, online security, etc.)
- Account information (tenure, contract type, payment method)
- Charges (monthly charges, total charges)
- Engineered features (service count, risk profile, family status, etc.)

## Configuration

You can modify settings in `backend/core/config.py`:
- API title and description
- CORS settings
- Model paths
- Risk level thresholds

## Error Handling

The API includes comprehensive error handling:
- Returns appropriate HTTP status codes
- Provides detailed error messages
- Validates input data using Pydantic models
- Handles model loading failures gracefully

## Development

### Adding New Endpoints

1. Add route handler in `backend/api/routes.py`
2. Create request/response models in `backend/models/`
3. Add business logic in `backend/services/` if needed

### Modifying Configuration

Update settings in `backend/core/config.py` to change:
- API metadata
- CORS policies
- Model paths
- Thresholds and constants

## License

MIT License
