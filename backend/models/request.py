"""
Request models for API endpoints
"""

from typing import List
from pydantic import BaseModel, Field


class CustomerData(BaseModel):
    """Input data for customer churn prediction"""

    gender: str = Field(..., description="Customer gender (Male/Female)")
    SeniorCitizen: int = Field(
        ..., description="Whether customer is senior citizen (0/1)"
    )
    Partner: str = Field(..., description="Whether customer has partner (Yes/No)")
    Dependents: str = Field(..., description="Whether customer has dependents (Yes/No)")
    tenure: int = Field(..., description="Number of months customer has stayed", ge=0)
    PhoneService: str = Field(
        ..., description="Whether customer has phone service (Yes/No)"
    )
    MultipleLines: str = Field(
        ..., description="Whether customer has multiple lines (Yes/No/No phone service)"
    )
    InternetService: str = Field(
        ..., description="Customer's internet service provider (DSL/Fiber optic/No)"
    )
    OnlineSecurity: str = Field(
        ...,
        description="Whether customer has online security (Yes/No/No internet service)",
    )
    OnlineBackup: str = Field(
        ...,
        description="Whether customer has online backup (Yes/No/No internet service)",
    )
    DeviceProtection: str = Field(
        ...,
        description="Whether customer has device protection (Yes/No/No internet service)",
    )
    TechSupport: str = Field(
        ...,
        description="Whether customer has tech support (Yes/No/No internet service)",
    )
    StreamingTV: str = Field(
        ...,
        description="Whether customer has streaming TV (Yes/No/No internet service)",
    )
    StreamingMovies: str = Field(
        ...,
        description="Whether customer has streaming movies (Yes/No/No internet service)",
    )
    Contract: str = Field(
        ..., description="Contract term (Month-to-month/One year/Two year)"
    )
    PaperlessBilling: str = Field(
        ..., description="Whether customer has paperless billing (Yes/No)"
    )
    PaymentMethod: str = Field(
        ...,
        description="Payment method (Electronic check/Mailed check/Bank transfer (automatic)/Credit card (automatic))",
    )
    MonthlyCharges: float = Field(..., description="Monthly charges amount", ge=0)
    TotalCharges: float = Field(..., description="Total charges amount", ge=0)

    class Config:
        json_schema_extra = {
            "example": {
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
                "TotalCharges": 1026.00,
            }
        }


class BatchPredictionRequest(BaseModel):
    """Request model for batch prediction"""

    customers: List[CustomerData]

