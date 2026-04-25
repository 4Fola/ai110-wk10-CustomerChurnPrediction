# tests/test_explainability.py
# Checkpoint 4 – Explainability safety

def test_forest_warning():
    from models.explain import forest_explanation_warning
    msg = forest_explanation_warning()
    assert "less interpretable" in msg.lower()