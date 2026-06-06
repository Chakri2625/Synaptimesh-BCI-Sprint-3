from app.validator import is_valid_confidence

def test_valid_confidence():
    assert is_valid_confidence(0.90) is True

def test_invalid_confidence():
    assert is_valid_confidence(0.50) is False