"""
API route handlers
"""

from fastapi import APIRouter, HTTPException
from backend.models.request import CustomerData, BatchPredictionRequest
from backend.models.response import (
    PredictionResponse,
    BatchPredictionResponse,
    ModelInfo,
    HealthResponse,
    RootResponse,
)
from backend.services.prediction import prediction_service
from backend.core.model_loader import model_manager
from backend.core.config import APP_TITLE, APP_VERSION

# Create router
router = APIRouter()


@router.get("/", response_model=RootResponse)
async def root():
    """Root endpoint with API information"""
    return RootResponse(
        message=APP_TITLE,
        version=APP_VERSION,
        status="active",
        endpoints={
            "POST /predict": "Single customer prediction",
            "POST /predict/batch": "Batch prediction for multiple customers",
            "GET /model/info": "Get model information",
            "GET /health": "Health check",
        },
    )


@router.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint"""
    model_loaded = model_manager.is_loaded()
    return HealthResponse(
        status="healthy" if model_loaded else "unhealthy",
        model_loaded=model_loaded,
    )


@router.get("/model/info", response_model=ModelInfo)
async def get_model_info():
    """Get model performance metrics and metadata"""
    try:
        metadata = model_manager.model_metadata
        return ModelInfo(
            model_name=metadata["model_name"],
            f1_score=metadata["f1_score"],
            accuracy=metadata["accuracy"],
            precision=metadata["precision"],
            recall=metadata["recall"],
            roc_auc=metadata["roc_auc"],
            n_features=metadata["n_features"],
            training_date=metadata["training_date"],
        )
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/predict", response_model=PredictionResponse)
async def predict_churn(customer: CustomerData):
    """
    Predict churn for a single customer

    Args:
        customer: Customer data for prediction

    Returns:
        Prediction results with churn probability and risk level
    """
    try:
        return prediction_service.predict_single(customer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")


@router.post("/predict/batch", response_model=BatchPredictionResponse)
async def predict_churn_batch(request: BatchPredictionRequest):
    """
    Predict churn for multiple customers

    Args:
        request: Batch prediction request with list of customers

    Returns:
        Batch prediction results with statistics
    """
    try:
        return prediction_service.predict_batch(request.customers)
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Batch prediction error: {str(e)}"
        )

