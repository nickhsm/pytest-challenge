import main


def test_main():
    """
    This funtions is some unittest for pytest
    """
    assert main.add(3, 3) == 6
    assert main.subtract(3, 3) == 0
    assert main.divide(3, 3) == 1
