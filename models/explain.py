# models/explain.py
# Checkpoint 2 – Explainability helpers

def risk_tier(probability: float) -> str:
    """
    Convert probability to risk tier.
    """
    if probability < 0.3:
        return "Low"
    if probability < 0.6:
        return "Medium"
    return "High"


def explain_decision_tree(model, feature_names, input_row):
    """
    Explain a single decision tree prediction.
    """
    tree = model.tree_
    node = 0
    explanation = []

    while tree.children_left[node] != tree.children_right[node]:
        feature_index = tree.feature[node]
        threshold = tree.threshold[node]
        feature_name = feature_names[feature_index]
        value = input_row[feature_name]

        if value <= threshold:
            explanation.append(
                f"{feature_name} ≤ {threshold:.2f}"
            )
            node = tree.children_left[node]
        else:
            explanation.append(
                f"{feature_name} > {threshold:.2f}"
            )
            node = tree.children_right[node]

    return explanation


def forest_explanation_warning():
    """
    Warn users that RF explanations are limited.
    """
    return (
        "Random Forest predictions are less interpretable. "
        "Only feature importance is shown."
    )