# models/train_model.py
# Checkpoint 2 – Model training and prediction

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier


FEATURE_COLUMNS = [
    "tenure",
    "monthly_charges",
    "total_charges",
    "contract_type",
    "internet_service",
]

TARGET_COLUMN = "churn"


def encode_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    One-hot encode categorical features.
    """
    return pd.get_dummies(df, columns=["contract_type", "internet_service"])


def split_data(df: pd.DataFrame):
    """
    Split features and target from an encoded dataframe.
    """
    X = df.drop(columns=[TARGET_COLUMN])
    y = df[TARGET_COLUMN]
    return X, y


def train_decision_tree(X, y):
    """
    Train a simple, interpretable decision tree.
    """
    model = DecisionTreeClassifier(
        max_depth=4,
        min_samples_leaf=10,
        random_state=42
    )
    model.fit(X, y)
    return model


def train_random_forest(X, y):
    """
    Train a random forest (less interpretable).
    """
    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=6,
        random_state=42
    )
    model.fit(X, y)
    return model


def train_model(df: pd.DataFrame, model_type="tree"):
    """
    High-level training function.
    """
    df_encoded = encode_features(df)
    X, y = split_data(df_encoded)

    if model_type == "forest":
        return train_random_forest(X, y)

    return train_decision_tree(X, y)


def predict_proba(model, input_df: pd.DataFrame) -> float:
    """
    Predict churn probability for a single customer.
    """
    prob = model.predict_proba(input_df)[0][1]
    return float(prob)