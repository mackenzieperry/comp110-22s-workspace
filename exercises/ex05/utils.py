"""Some utility functions for lists."""

__author__ = "730468950"


def only_evens(sent_list: list[int]) -> list[int]:
    """Given a list of ints, prints only the even numbers."""
    even_numbers: list[int] = list()
    i: int = 0
    while i < len(sent_list):
        if sent_list[i] % 2 == 0:
            even_numbers.append(sent_list[i])
        i += 1
    return even_numbers


def sub(sent_list: list[int], start_index: int, end_index) -> list[int]:
    """Given a list and a start and end index it returns a sub list of the elements within those indexes."""
    sub_list: list[int] = list()
    if start_index >= 0:
        i: int = start_index
    else:
        i: int = 0
    if end_index > len(sent_list) - 1:
        while i < len(sent_list):
            sub_list.append(sent_list[i])
            i += 1
    else:
        while i < end_index:
            sub_list.append(sent_list[i])
            i += 1
    return sub_list


def concat(sent_list1: list[int], sent_list2: list[int]) -> list[int]:
    """Adds two lists together."""
    joined_list: list[int] = list()
    i: int = 0
    while i < len(sent_list1):
        joined_list.append(sent_list1[i])
        i += 1
    i = 0
    while i < len(sent_list2):
        joined_list.append(sent_list2[i])
        i += 1
    return joined_list