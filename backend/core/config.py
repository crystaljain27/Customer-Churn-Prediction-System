"""
Configuration settings for the application
"""

import os
from pathlib import Path

# Application settings
APP_TITLE = "Customer Churn Prediction API"
APP_DESCRIPTION = "API for predicting customer churn using XGBoost model"
APP_VERSION = "1.0.0"

# CORS settings - Allow all origins for deployment
ALLOW_ORIGINS = ["*"]
ALLOW_CREDENTIALS = True
ALLOW_METHODS = ["*"]
ALLOW_HEADERS = ["*"]

# Model settings
PROJECT_ROOT = Path(__file__).parent.parent.parent
MODELS_DIR = PROJECT_ROOT / "models"

# Risk level thresholds
RISK_THRESHOLD_LOW = 0.3
RISK_THRESHOLD_MEDIUM = 0.6

# Environment settings
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
DEBUG = ENVIRONMENT == "development"

