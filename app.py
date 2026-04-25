# app.py
# Checkpoint 3 – Streamlit GUI for Churn Prediction

import streamlit as st
import pandas as pd

from data.data_loader import load_and_validate
from models.train_model import train_model, predict_proba, encode_features
from models.explain import risk_tier, explain_decision_tree, forest_explanation_warning


# -----------------------------
# App setup
# -----------------------------
st.set_page_config(page_title="Churn Prediction AI", layout="wide")
st.title("📉 Customer Churn Prediction")
st.caption(
    "An explainable AI system that predicts customer churn and flags high-risk cases for human review."
)


# -----------------------------
# Sidebar – configuration
# -----------------------------
st.sidebar.header("Configuration")

data_source = st.sidebar.radio(
    "Data source",
    ["Use sample dataset", "Upload CSV"]
)

model_choice = st.sidebar.radio(
    "Model type",
    ["Decision Tree (explainable)", "Random Forest (less interpretable)"]
)

st.sidebar.divider()


# -----------------------------
# Load dataset
# -----------------------------
if data_source == "Use sample dataset":
    data_path = "data/sample_churn.csv"
    df = load_and_validate(data_path)
    st.sidebar.success("Sample dataset loaded")

else:
    uploaded = st.sidebar.file_uploader("Upload CSV", type="csv")
    if uploaded is None:
        st.warning("Please upload a CSV file to continue.")
        st.stop()
    df = load_and_validate(uploaded)
    st.sidebar.success("Custom dataset loaded")


st.subheader("Dataset Preview")
st.dataframe(df.head())


# -----------------------------
# Train model
# -----------------------------
model_type = "tree" if model_choice.startswith("Decision") else "forest"
model = train_model(df, model_type=model_type)

if model_type == "forest":
    st.info(forest_explanation_warning())


# -----------------------------
# Manual prediction
# -----------------------------
st.divider()
st.subheader("🔍 Manual Customer Prediction")

with st.form("manual_input"):
    tenure = st.number_input("Tenure (months)", min_value=0, value=12)
    monthly = st.number_input("Monthly Charges", min_value=0.0, value=70.0)
    total = st.number_input("Total Charges", min_value=0.0, value=800.0)
    contract = st.selectbox(
        "Contract Type",
        ["month-to-month", "one-year", "two-year"]
    )
    internet = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber", "None"]
    )

    submit = st.form_submit_button("Predict churn")

if submit:
    input_df = pd.DataFrame([{
        "tenure": tenure,
        "monthly_charges": monthly,
        "total_charges": total,
        "contract_type": contract,
        "internet_service": internet,
    }])

    input_encoded = encode_features(
        pd.concat([df.drop(columns=["churn"]), input_df], axis=0)
    ).tail(1)

    prob = predict_proba(model, input_encoded)
    tier = risk_tier(prob)

    st.subheader("Prediction Result")
    st.metric("Churn Probability", f"{prob:.2%}")
    st.metric("Risk Tier", tier)

    # -----------------------------
    # Reliability guardrail
    # -----------------------------
    if tier == "High":
        st.error(
            "⚠️ High churn risk detected. "
            "Human review is recommended before taking action."
        )

    elif tier == "Medium":
        st.warning(
            "⚠️ Moderate churn risk. "
            "Consider reviewing this customer profile."
        )

    else:
        st.success("✅ Low churn risk detected.")

    # -----------------------------
    # Explainability
    # -----------------------------
    st.subheader("Explanation")

    if model_type == "tree":
        explanation = explain_decision_tree(
            model,
            feature_names=input_encoded.columns.tolist(),
            input_row=input_encoded.iloc[0]
        )

        for step in explanation:
            st.write(f"- {step}")

    else:
        st.write(
            "Feature importance can be used for general insights, "
            "but individual decisions are not directly traceable."
        )


# -----------------------------
# Batch prediction
# -----------------------------
st.divider()
st.subheader("📂 Batch Prediction")

batch_file = st.file_uploader(
    "Upload CSV for batch prediction (same schema, no churn column)",
    type="csv",
    key="batch"
)

if batch_file:
    batch_df = pd.read_csv(batch_file)

    batch_encoded = encode_features(
        pd.concat([df.drop(columns=["churn"]), batch_df], axis=0)
    ).tail(len(batch_df))

    probs = model.predict_proba(batch_encoded)[:, 1]
    results = batch_df.copy()
    results["churn_probability"] = probs
    results["risk_tier"] = [risk_tier(p) for p in probs]

    st.dataframe(results)

    st.download_button(
        "Download Results",
        results.to_csv(index=False),
        file_name="churn_predictions.csv"
    )