from src.multiply_utils import multiply


def test_multiply():
    assert multiply(3, 6) == 18
    assert multiply(-1, 5) == -5
    assert multiply(2, 4) == 8
