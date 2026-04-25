# tests/test_risk_logic.py
# Checkpoint 4 – Risk tier reliability tests

from models.explain import risk_tier


def test_low_risk():
    assert risk_tier(0.1) == "Low"


def test_medium_risk():
    assert risk_tier(0.4) == "Medium"


def test_high_risk():
    assert risk_tier(0.9) == "High"
