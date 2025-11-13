# Backend Architecture

## Overview

The backend follows a clean, modular architecture with clear separation of concerns.

## Directory Structure

```
backend/
├── main.py                      # Entry point - FastAPI app initialization
│
├── api/                         # API Layer
│   ├── __init__.py
│   └── routes.py               # All endpoint handlers
│
├── core/                        # Core Configuration Layer
│   ├── __init__.py
│   ├── config.py               # Application settings & constants
│   └── model_loader.py         # Singleton model manager
│
├── models/                      # Data Models Layer
│   ├── __init__.py
│   ├── request.py              # Pydantic request models
│   └── response.py             # Pydantic response models
│
└── services/                    # Business Logic Layer
    ├── __init__.py
    ├── preprocessing.py        # Feature engineering
    └── prediction.py           # Prediction logic
```

## Layer Responsibilities

### 1. Entry Point (`main.py`)
- Initialize FastAPI application
- Configure middleware (CORS)
- Include routers
- Handle startup/shutdown events
- Load model artifacts on startup

### 2. API Layer (`api/`)
- **routes.py**: Define all API endpoints
  - Root endpoint (`/`)
  - Health check (`/health`)
  - Model info (`/model/info`)
  - Single prediction (`/predict`)
  - Batch prediction (`/predict/batch`)

### 3. Core Layer (`core/`)
- **config.py**: Centralized configuration
  - App metadata (title, version)
  - CORS settings
  - File paths
  - Constants (risk thresholds)

- **model_loader.py**: Model management
  - Singleton pattern for model artifacts
  - Load and cache ML model
  - Load and cache preprocessors
  - Provide thread-safe access

### 4. Models Layer (`models/`)
- **request.py**: Input validation
  - `CustomerData`: Single customer input
  - `BatchPredictionRequest`: Multiple customers

- **response.py**: Output structure
  - `PredictionResponse`: Single prediction
  - `BatchPredictionResponse`: Batch results
  - `ModelInfo`: Model metadata
  - `HealthResponse`: Health status
  - `RootResponse`: API information

### 5. Services Layer (`services/`)
- **preprocessing.py**: Data transformation
  - Feature engineering
  - Categorical encoding
  - Feature scaling
  - Match training pipeline

- **prediction.py**: Business logic
  - Single prediction
  - Batch prediction
  - Risk level calculation
  - Orchestrate preprocessing + model inference

## Data Flow

### Single Prediction Flow

```
Client Request
    ↓
routes.py (predict_churn)
    ↓
prediction_service.predict_single()
    ↓
DataPreprocessor.preprocess()
    ├─ _engineer_features()
    ├─ _encode_features()
    └─ scale features
    ↓
model_manager.model.predict()
    ↓
Calculate risk level
    ↓
PredictionResponse
    ↓
Client Response
```

### Batch Prediction Flow

```
Client Request (multiple customers)
    ↓
routes.py (predict_churn_batch)
    ↓
prediction_service.predict_batch()
    ├─ Loop through customers
    ├─ predict_single() for each
    └─ Calculate statistics
    ↓
BatchPredictionResponse
    ↓
Client Response
```

## Design Patterns

### 1. Singleton Pattern
- **ModelManager**: Ensures single instance of model artifacts
- Benefits:
  - Memory efficient (load once)
  - Thread-safe access
  - Centralized state

### 2. Service Pattern
- **PredictionService**: Encapsulates prediction logic
- **DataPreprocessor**: Encapsulates preprocessing logic
- Benefits:
  - Reusable business logic
  - Easy to test
  - Clear responsibilities

### 3. Dependency Injection
- Services use model_manager singleton
- Routes use service instances
- Benefits:
  - Loose coupling
  - Easy to mock for testing
  - Flexible configuration

## Key Components

### ModelManager (Singleton)
```python
model_manager = ModelManager()
model_manager.load_artifacts()

# Access loaded artifacts
model = model_manager.model
scaler = model_manager.scaler
encoders = model_manager.label_encoders
```

### PredictionService
```python
prediction_service = PredictionService()

# Single prediction
result = prediction_service.predict_single(customer_data)

# Batch prediction
results = prediction_service.predict_batch(customers)
```

### DataPreprocessor
```python
preprocessor = DataPreprocessor()

# Preprocess customer data
processed_df = preprocessor.preprocess(customer_data)
```

## Configuration Management

All configuration is centralized in `core/config.py`:

```python
# Application settings
APP_TITLE = "Customer Churn Prediction API"
APP_VERSION = "1.0.0"

# Model paths
MODELS_DIR = Path(__file__).parent.parent.parent / "models"

# Risk thresholds
RISK_THRESHOLD_LOW = 0.3
RISK_THRESHOLD_MEDIUM = 0.6
```

## Benefits of This Architecture

1. **Maintainability**
   - Clear separation of concerns
   - Easy to locate and modify code
   - Changes in one layer don't affect others

2. **Testability**
   - Each component can be tested independently
   - Easy to mock dependencies
   - Clear interfaces

3. **Scalability**
   - Easy to add new endpoints
   - Easy to add new services
   - Modular components

4. **Readability**
   - Small, focused files
   - Clear naming conventions
   - Logical organization

5. **Reusability**
   - Services can be used across multiple routes
   - Preprocessing logic is centralized
   - Models are shared

## Adding New Features

### Add a New Endpoint

1. Define request/response models in `models/`
2. Add business logic in `services/` (if needed)
3. Create route handler in `api/routes.py`
4. Document in README

### Add New Preprocessing Step

1. Modify `services/preprocessing.py`
2. Update feature engineering method
3. Ensure consistency with training

### Modify Risk Thresholds

1. Update constants in `core/config.py`
2. No code changes needed elsewhere

## Error Handling Strategy

- **API Layer**: Catch exceptions, return HTTP errors
- **Service Layer**: Raise domain-specific exceptions
- **Core Layer**: Raise loading/configuration errors
- **Models Layer**: Pydantic validation errors

## Best Practices

1. **Single Responsibility**: Each module has one clear purpose
2. **DRY (Don't Repeat Yourself)**: Shared logic is centralized
3. **Configuration over Code**: Settings in config files
4. **Type Hints**: All functions have type annotations
5. **Documentation**: Docstrings for all public methods
6. **Constants**: Magic numbers are named constants

## Performance Considerations

- **Model Loading**: Done once at startup (singleton)
- **Preprocessing**: Optimized with pandas/numpy
- **Batch Processing**: Reuses preprocessing logic efficiently
- **Response Caching**: Can be added at route level if needed

## Security Considerations

- **Input Validation**: Pydantic models validate all inputs
- **CORS**: Configurable in `config.py`
- **Error Messages**: Don't leak sensitive information
- **Model Files**: Kept outside API directory

## Future Enhancements

Potential improvements to consider:
- Add authentication/authorization
- Add rate limiting
- Add caching layer (Redis)
- Add monitoring/metrics
- Add async preprocessing
- Add model versioning
- Add A/B testing support

