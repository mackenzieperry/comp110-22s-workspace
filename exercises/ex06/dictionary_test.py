"""Unit tests for dictionary functions."""

__author__ = "730468950"

from exercises.ex06.dictionary import invert, favorite_color, count
import pytest


def test_invert_normal_use() -> None:
    """Test invert function in a normal use case."""
    assert invert({'a': '1', 'b': '2', 'c': '3'}) == {'1': 'a', '2': 'b', '3': 'c'}


def test_invert_longer_string() -> None:
    """Tests the invert function with long keys and values."""
    assert invert({'Jon': 'Smith', 'Ashley': 'Johnson'}) == {'Smith': 'Jon', 'Johnson': 'Ashley'}


def test_invert_empty() -> None:
    """Tests invert() if send an empty dictionary."""
    assert invert({}) == {}


def test_invert_double_keys() -> None:
    """Test invert if return dict would have double keys."""
    with pytest.raises(KeyError):
        invert({'a': '1', 'b': '1', 'c': '1'})


def test_favorite_color_normal_use() -> None:
    """Tests favorite_color like a normal use case."""
    assert favorite_color({"ellie": "Blue", "howie": "Green", "howard": "Red", "Joel": "Red", "Hidie": "Yellow"}) == "Red"


def test_favorite_color_empty_dict() -> None:
    """Tests if the sent dict if empty, if return value is empty."""
    assert favorite_color({}) == ""


def test_favorite_colors_two_maxes() -> None:
    """Tests if function gets sent a dict that has two mode colors."""
    assert favorite_color({'A': 'blue', 'B': 'Red', 'C': 'Red', 'D': 'blue'}) == 'blue'


def test_count_empty() -> None:
    """Tests when count gets set an empty list."""
    assert count([]) == {}


def test_count_normal_use() -> None:
    """Tests count under normal use."""
    assert count(['1', '1', '2', '3', '2', '4', '2']) == {'1': 2, '2': 3, '3': 1, '4': 1}


def test_count_longer_strings() -> None:
    """Tests count using longer strings."""
    assert count(['break', 'cot', '1', 'hello', 'cot', 'cot', 'hello', 'break']) == {'break': 2, 'cot': 3, '1': 1, 'hello': 2}