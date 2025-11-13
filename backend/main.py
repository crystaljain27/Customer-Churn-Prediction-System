"""
FastAPI application for Customer Churn Prediction
Entry point for the application
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.core.config import (
    APP_TITLE,
    APP_DESCRIPTION,
    APP_VERSION,
    ALLOW_ORIGINS,
    ALLOW_CREDENTIALS,
    ALLOW_METHODS,
    ALLOW_HEADERS,
)
from backend.core.model_loader import model_manager
from backend.api.routes import router

# Initialize FastAPI app
app = FastAPI(
    title=APP_TITLE,
    description=APP_DESCRIPTION,
    version=APP_VERSION,
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOW_ORIGINS,
    allow_credentials=ALLOW_CREDENTIALS,
    allow_methods=ALLOW_METHODS,
    allow_headers=ALLOW_HEADERS,
)

# Include routes
app.include_router(router)


@app.on_event("startup")
async def startup_event():
    """Load model artifacts on application startup"""
    print("🚀 Starting Customer Churn Prediction API...")
    model_manager.load_artifacts()
    print("✅ Application ready!")


@app.on_event("shutdown")
async def shutdown_event():
    """Cleanup on application shutdown"""
    print("👋 Shutting down Customer Churn Prediction API...")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
