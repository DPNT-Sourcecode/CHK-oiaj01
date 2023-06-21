import pytest

from solutions.HLO import hello_solution

def test_says_hello() -> None:
    assert hello_solution.hello("John") == "Hello, John!"