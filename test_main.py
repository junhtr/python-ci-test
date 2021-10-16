"""Test for main.py"""
import main


def test_main() -> None:
    """test_main"""
    assert main.main() == 2


def test_main2() -> None:
    """test_main2"""
    assert main.main2() == 3
