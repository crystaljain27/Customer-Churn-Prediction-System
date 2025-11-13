"""
Model loading and management
"""

import pickle
from pathlib import Path
from typing import Any, Dict, Optional

from backend.core.config import MODELS_DIR


class ModelManager:
    """Singleton class to manage ML model artifacts"""

    _instance: Optional["ModelManager"] = None
    _model: Any = None
    _scaler: Any = None
    _label_encoders: Dict[str, Any] = None
    _feature_names: list = None
    _model_metadata: Dict[str, Any] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def load_artifacts(self) -> None:
        """Load all model artifacts from pickle files"""
        try:
            with open(MODELS_DIR / "xgboost_model.pkl", "rb") as f:
                self._model = pickle.load(f)

            with open(MODELS_DIR / "scaler.pkl", "rb") as f:
                self._scaler = pickle.load(f)

            with open(MODELS_DIR / "label_encoders.pkl", "rb") as f:
                self._label_encoders = pickle.load(f)

            with open(MODELS_DIR / "feature_names.pkl", "rb") as f:
                self._feature_names = pickle.load(f)

            with open(MODELS_DIR / "model_metadata.pkl", "rb") as f:
                self._model_metadata = pickle.load(f)

            print("✓ All model artifacts loaded successfully")
        except Exception as e:
            print(f"Error loading model artifacts: {e}")
            raise

    @property
    def model(self):
        """Get the loaded model"""
        if self._model is None:
            raise RuntimeError("Model not loaded. Call load_artifacts() first.")
        return self._model

    @property
    def scaler(self):
        """Get the loaded scaler"""
        if self._scaler is None:
            raise RuntimeError("Scaler not loaded. Call load_artifacts() first.")
        return self._scaler

    @property
    def label_encoders(self):
        """Get the loaded label encoders"""
        if self._label_encoders is None:
            raise RuntimeError("Label encoders not loaded. Call load_artifacts() first.")
        return self._label_encoders

    @property
    def feature_names(self):
        """Get the feature names"""
        if self._feature_names is None:
            raise RuntimeError("Feature names not loaded. Call load_artifacts() first.")
        return self._feature_names

    @property
    def model_metadata(self):
        """Get the model metadata"""
        if self._model_metadata is None:
            raise RuntimeError("Model metadata not loaded. Call load_artifacts() first.")
        return self._model_metadata

    def is_loaded(self) -> bool:
        """Check if model artifacts are loaded"""
        return self._model is not None


# Create singleton instance
model_manager = ModelManager()

