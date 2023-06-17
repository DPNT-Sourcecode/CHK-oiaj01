import pytest

from solutions.SUM import sum_solution


class TestSum():
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3

    def test_sum_with_zero(self):
        assert sum_solution.compute(0, 0) == 0

    def test_sum_with_negative(self):
        assert sum_solution.compute(-1, -2) == -3

    def test_sum_with_positive_and_negative(self):
        assert sum_solution.compute(-1, 2) == 1

    def test_sum_raises_exception_with_invalid_input(self):
        with pytest.raises(AssertionError):
            sum_solution.compute("a", 1)

        with pytest.raises(AssertionError):
            sum_solution.compute(1, "a")
