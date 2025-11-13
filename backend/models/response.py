"""
Response models for API endpoints
"""

from typing import List, Dict
from pydantic import BaseModel, Field


class PredictionResponse(BaseModel):
    """Response model for prediction"""

    churn_prediction: int = Field(..., description="Predicted churn (0=No, 1=Yes)")
    churn_probability: float = Field(..., description="Probability of churn")
    churn_label: str = Field(..., description="Churn label (No Churn/Churn)")
    risk_level: str = Field(..., description="Risk level (Low/Medium/High)")

    class Config:
        json_schema_extra = {
            "example": {
                "churn_prediction": 1,
                "churn_probability": 0.78,
                "churn_label": "Churn",
                "risk_level": "High",
            }
        }


class BatchPredictionResponse(BaseModel):
    """Response model for batch prediction"""

    predictions: List[PredictionResponse]
    total_customers: int
    predicted_churners: int
    churn_rate: float


class ModelInfo(BaseModel):
    """Model information response"""

    model_name: str
    f1_score: float
    accuracy: float
    precision: float
    recall: float
    roc_auc: float
    n_features: int
    training_date: str


class HealthResponse(BaseModel):
    """Health check response"""

    status: str
    model_loaded: bool


class RootResponse(BaseModel):
    """Root endpoint response"""

    message: str
    version: str
    status: str
    endpoints: Dict[str, str]

