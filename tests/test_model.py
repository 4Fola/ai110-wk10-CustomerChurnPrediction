# tests/test_model.py
# Checkpoint 2 – Model sanity tests

import pandas as pd
from models.train_model import train_model, predict_proba


def test_model_trains_and_predicts():
    df = pd.DataFrame({
        "tenure": [1, 12],
        "monthly_charges": [80, 50],
        "total_charges": [80, 600],
        "contract_type": ["month-to-month", "one-year"],
        "internet_service": ["Fiber", "DSL"],
        "churn": [1, 0],
    })

    model = train_model(df, model_type="tree")

    input_df = pd.get_dummies(df.drop(columns=["churn"]))
    prob = predict_proba(model, input_df.iloc[[0]])

    assert 0.0 <= prob <= 1.0