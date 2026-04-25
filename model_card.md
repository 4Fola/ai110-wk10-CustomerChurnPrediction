# 👉 [Model Card](model_card.md) | [AI Bill of Materials](AI_Bill_of_Materials.md) | 

# Model Card – Customer Churn Prediction AI

## System Overview
This system predicts customer churn risk using structured customer data.
It is designed to support decision‑making, not automate it.

## Intended Use
- Identify customers at risk of churn
- Support retention and review workflows

## Not Intended For
- Automated customer termination
- Decisions without human oversight

## Models Used
- Decision Tree (default, explainable)
- Random Forest (optional, less interpretable)

## Inputs
Customer attributes such as tenure, charges, contract type, and internet service.

## Outputs
- Churn probability
- Risk tier (Low / Medium / High)
- Explanation (Decision Tree only)

## Performance Notes
The model is trained on small, illustrative datasets.
Predictions should be treated as advisory signals.

## Failure Modes
- Oversimplification of complex behavior
- Reduced explainability in Random Forest mode

## Human-in-the-Loop Triggers
- High risk tier
- Random Forest selection
- Ambiguous customer profiles

## Ethical Considerations
The system avoids demographic attributes and does not infer protected characteristics.