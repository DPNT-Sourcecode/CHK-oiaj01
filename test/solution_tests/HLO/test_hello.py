import pytest

from solutions.HLO import hello_solution


def test_refuses_non_string() -> None:
    with pytest.raises(AssertionError):
        hello_solution.hello(1)

def test_says_hello() -> None:
    assert hello_solution.hello("John") == "Hello, World!"