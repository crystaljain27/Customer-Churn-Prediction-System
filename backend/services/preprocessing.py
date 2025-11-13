"""
Data preprocessing and feature engineering
"""

import pandas as pd
from backend.models.request import CustomerData
from backend.core.model_loader import model_manager


class DataPreprocessor:
    """Handle all data preprocessing and feature engineering"""

    @staticmethod
    def preprocess(customer_data: CustomerData) -> pd.DataFrame:
        """
        Preprocess input data to match training data format

        Args:
            customer_data: Customer data from API request

        Returns:
            Preprocessed and scaled DataFrame ready for prediction
        """
        # Convert to dictionary and create DataFrame
        data = customer_data.dict()
        df = pd.DataFrame([data])

        # Apply feature engineering
        df = DataPreprocessor._engineer_features(df)

        # Encode categorical variables
        df = DataPreprocessor._encode_features(df)

        # Ensure correct feature order
        df = df[model_manager.feature_names]

        # Scale features
        df_scaled = model_manager.scaler.transform(df)
        df_scaled = pd.DataFrame(df_scaled, columns=model_manager.feature_names)

        return df_scaled

    @staticmethod
    def _engineer_features(df: pd.DataFrame) -> pd.DataFrame:
        """
        Create engineered features matching the training process

        Args:
            df: Input DataFrame

        Returns:
            DataFrame with engineered features
        """
        # 1. Service Count
        service_cols = [
            "PhoneService",
            "InternetService",
            "OnlineSecurity",
            "OnlineBackup",
            "DeviceProtection",
            "TechSupport",
            "StreamingTV",
            "StreamingMovies",
        ]

        df["ServiceCount"] = 0
        for col in service_cols:
            if col == "PhoneService":
                df["ServiceCount"] += (df[col] == "Yes").astype(int)
            elif col == "InternetService":
                df["ServiceCount"] += (df[col] != "No").astype(int)
            else:
                df["ServiceCount"] += (df[col] == "Yes").astype(int)

        # 2. Average Monthly Rate
        df["AvgMonthlyRate"] = df["TotalCharges"] / df["tenure"].replace(0, 1)

        # 3. Premium Service Count
        premium_services = [
            "OnlineSecurity",
            "OnlineBackup",
            "DeviceProtection",
            "TechSupport",
        ]
        df["PremiumServiceCount"] = sum(
            [(df[col] == "Yes").astype(int) for col in premium_services]
        )
        df["HasPremiumServices"] = (df["PremiumServiceCount"] > 0).map(
            {True: "Yes", False: "No"}
        )

        # 4. Has Streaming
        df["HasStreaming"] = (
            (df["StreamingTV"] == "Yes") | (df["StreamingMovies"] == "Yes")
        ).map({True: "Yes", False: "No"})

        # 5. Value Segment
        df["ValueSegment"] = pd.cut(
            df["MonthlyCharges"],
            bins=[0, 35, 70, 120],
            labels=["Low Value", "Medium Value", "High Value"],
        )

        # 6. High Risk Profile
        df["HighRiskProfile"] = (
            (df["Contract"] == "Month-to-month")
            & (df["PaymentMethod"] == "Electronic check")
        ).map({True: "Yes", False: "No"})

        # 7. Family Customer
        df["FamilyCustomer"] = (
            (df["Partner"] == "Yes") | (df["Dependents"] == "Yes")
        ).map({True: "Yes", False: "No"})

        # 8. Interaction features
        df["Tenure_MonthlyCharges"] = df["tenure"] * df["MonthlyCharges"]
        df["Tenure_ServiceCount"] = df["tenure"] * df["ServiceCount"]
        df["MonthlyCharges_ServiceCount"] = df["MonthlyCharges"] * df["ServiceCount"]

        return df

    @staticmethod
    def _encode_features(df: pd.DataFrame) -> pd.DataFrame:
        """
        Encode categorical variables using saved label encoders

        Args:
            df: DataFrame with categorical features

        Returns:
            DataFrame with encoded categorical features
        """
        categorical_cols = [
            "gender",
            "Partner",
            "Dependents",
            "PhoneService",
            "MultipleLines",
            "InternetService",
            "OnlineSecurity",
            "OnlineBackup",
            "DeviceProtection",
            "TechSupport",
            "StreamingTV",
            "StreamingMovies",
            "Contract",
            "PaperlessBilling",
            "PaymentMethod",
            "HasPremiumServices",
            "HasStreaming",
            "HighRiskProfile",
            "FamilyCustomer",
            "ValueSegment",
        ]

        label_encoders = model_manager.label_encoders

        for col in categorical_cols:
            if col in df.columns and col in label_encoders:
                df[col] = label_encoders[col].transform(df[col].astype(str))

        return df

