"""
Prediction service for churn prediction
"""

from typing import List
from backend.models.request import CustomerData
from backend.models.response import PredictionResponse, BatchPredictionResponse
from backend.services.preprocessing import DataPreprocessor
from backend.core.model_loader import model_manager
from backend.core.config import RISK_THRESHOLD_LOW, RISK_THRESHOLD_MEDIUM


class PredictionService:
    """Handle prediction logic"""

    def __init__(self):
        self.preprocessor = DataPreprocessor()

    def predict_single(self, customer_data: CustomerData) -> PredictionResponse:
        """
        Predict churn for a single customer

        Args:
            customer_data: Customer data from API request

        Returns:
            PredictionResponse with prediction results
        """
        # Preprocess input
        processed_data = self.preprocessor.preprocess(customer_data)

        # Make prediction
        prediction = model_manager.model.predict(processed_data)[0]
        probability = model_manager.model.predict_proba(processed_data)[0][1]

        # Determine risk level
        risk_level = self._get_risk_level(probability)

        return PredictionResponse(
            churn_prediction=int(prediction),
            churn_probability=float(probability),
            churn_label="Churn" if prediction == 1 else "No Churn",
            risk_level=risk_level,
        )

    def predict_batch(
        self, customers: List[CustomerData]
    ) -> BatchPredictionResponse:
        """
        Predict churn for multiple customers

        Args:
            customers: List of customer data

        Returns:
            BatchPredictionResponse with all predictions and statistics
        """
        predictions = []

        for customer in customers:
            prediction = self.predict_single(customer)
            predictions.append(prediction)

        # Calculate statistics
        total_customers = len(predictions)
        predicted_churners = sum(1 for p in predictions if p.churn_prediction == 1)
        churn_rate = predicted_churners / total_customers if total_customers > 0 else 0

        return BatchPredictionResponse(
            predictions=predictions,
            total_customers=total_customers,
            predicted_churners=predicted_churners,
            churn_rate=round(churn_rate, 4),
        )

    @staticmethod
    def _get_risk_level(probability: float) -> str:
        """
        Determine risk level based on probability

        Args:
            probability: Churn probability

        Returns:
            Risk level string (Low/Medium/High)
        """
        if probability < RISK_THRESHOLD_LOW:
            return "Low"
        elif probability < RISK_THRESHOLD_MEDIUM:
            return "Medium"
        else:
            return "High"


# Create singleton instance
prediction_service = PredictionService()

