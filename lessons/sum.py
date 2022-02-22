"""Exampl eof writing a test subject."""


def sum(xs: list[float]) -> float:
    """Computes the sum of a list."""
    total: float = 0.0
    for item in xs:
        total += item
    return total
