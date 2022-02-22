"""Tests for utils functions."""

__author__ = "730468950"

from exercises.ex05.utils import only_evens, sub, concat


# Testing only_evens()
def test_only_evens_empty() -> None:
    """Tests if sent an empty list, and empty list is returned."""
    assert only_evens([]) == []


def test_only_evens_no_evens() -> None:
    """Checks if an empty list is returned when no even numbers are given."""
    assert only_evens([1, 3, 5, 7]) == []


def test_only_evens_use_case() -> None:
    """Checks if only evens are returned with a normal use case."""
    assert only_evens([1, 2, 4, 7, 8]) == [2, 4, 8]


def test_only_evens_with_zero() -> None:
    """Checks normal use case with a zero (which according to my research can be classified as an even number)."""
    assert only_evens([0, 6, 0, 8, 26, 7]) == [0, 6, 0, 8, 26]


# Testing sub()
def test_sub_with_end_greater_than_start() -> None:
    """Test if end > start parameters are given in wrong order an empty list will be returned."""
    assert sub([3, 4, 6, 7, 8], 5, 3) == []


def test_sub_if_indexes_out_of_range() -> None:
    """Test sub if end index is out of range, that return will just be to end of list."""
    assert sub([0, 1, 2, 3, 4, 5, 6], 2, 22) == [2, 3, 4, 5, 6]


def test_sub_normal_use() -> None:
    """Test sub with normal start and end indexes."""
    assert sub([0, 1, 2, 3, 4, 5, 6, 7, 8], 3, 7) == [3, 4, 5, 6]


def test_sub_with_negative_numbers() -> None:
    """Test sub with negative numbers in the array."""
    assert sub([-1, -4, -8, 3, 12, 7, -30], 0, 5) == [-1, -4, -8, 3, 12]


# Testing concat()
def test_concat_empty_list() -> None:
    """Tests when you add an empty string."""
    assert concat([], [1, 2, 4, 8]) == [1, 2, 4, 8]


def test_concat_normal_use() -> None:
    """Test with two normal arrays."""
    assert concat([2, 4, 6, 7, 8, 8, 12], [0, 5, 6]) == [2, 4, 6, 7, 8, 8, 12, 0, 5, 6]


def test_concat_second_array_longer() -> None:
    """Tests concat if the second array is the longer one."""
    assert concat([-1, 0, 4, 4], [2, 2, 2, 2, 6, 33]) == [-1, 0, 4, 4, 2, 2, 2, 2, 6, 33]