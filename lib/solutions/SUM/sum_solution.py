# noinspection PyShadowingBuiltins,PyUnusedLocal
from typing import Union


NumberLike = Union[int, float]


def compute(x: NumberLike, y: NumberLike) -> NumberLike:
    """
    Adds two numbers together.

    Parameters
    ----------
    x : Union[int, float]
        The first number to add.
    y : Union[int, float]
        The second number to add.

    Returns
    -------
    Union[int, float]

    Raises
    ------
    AssertionError
        If either of the inputs are not ints or floats.

    """
    assert all([isinstance(x, (int, float)), isinstance(y, (int, float))]), "Inputs must be ints or floats."

    return x + y

