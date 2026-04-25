# tests/test_data_loader.py
# Checkpoint 1 – Data validation tests

import pandas as pd
import pytest
from data.data_loader import validate_schema, validate_values


def test_missing_columns():
    df = pd.DataFrame({"tenure": [1, 2, 3]})
    with pytest.raises(ValueError):
        validate_schema(df)


def test_invalid_churn_values():
    df = pd.DataFrame({
        "tenure": [1],
        "monthly_charges": [50],
        "total_charges": [50],
        "contract_type": ["month-to-month"],
        "internet_service": ["DSL"],
        "churn": [2],
    })
    with pytest.raises(ValueError):
        validate_values(df)