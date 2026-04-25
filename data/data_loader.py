# data/data_loader.py
# Checkpoint 1 – Data loading and validation

import pandas as pd

REQUIRED_COLUMNS = {
    "tenure",
    "monthly_charges",
    "total_charges",
    "contract_type",
    "internet_service",
    "churn",
}


def load_csv(path: str) -> pd.DataFrame:
    """
    Load a CSV file from disk.
    Raises a clear error if loading fails.
    """
    try:
        return pd.read_csv(path)
    except Exception as e:
        raise ValueError(f"Failed to load CSV: {e}")


def validate_schema(df: pd.DataFrame) -> None:
    """
    Ensure the dataset contains all required columns.
    """
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")


def validate_values(df: pd.DataFrame) -> None:
    """
    Basic sanity checks for data quality.
    """
    if df.empty:
        raise ValueError("Dataset is empty")

    if not set(df["churn"].unique()).issubset({0, 1}):
        raise ValueError("Churn column must contain only 0 or 1")


def load_and_validate(path: str) -> pd.DataFrame:
    """
    High-level helper used by the app.
    """
    df = load_csv(path)
    validate_schema(df)
    validate_values(df)
    return df
