# AI Bill of Materials (AI-BOM)

## Algorithms
- Decision Tree Classifier
- Random Forest Classifier

## Libraries
- pandas
- scikit-learn
- streamlit

## Data
- Sample telecom-style churn dataset
- User-uploaded CSVs (validated before use)

## Assumptions
- Input data reflects historical patterns
- Relationships are stable over time

## Risks
- Model drift if business context changes
- Over-reliance on probability scores

## Mitigations
- Explainability-first defaults
- Conservative thresholds
- Human review prompts

## Governance
- Explicit documentation
- Clear warnings in UI
- No hidden automation