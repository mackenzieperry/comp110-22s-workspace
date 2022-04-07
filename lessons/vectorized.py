from __future__ import annotations
from typing import Union


class StrArray:
    items: list[str]

    def __init__(self, items):
        self.items = items

    def __repr__(self) -> str:
        return f"StrArray({self.items})"

    def __add__(self, rhs: Union[str, StrArray]) -> StrArray:
        """Add is a vectorized operation that applies to all items. When
        rhs is a str, it is concatenated to every item in a new Str Array."""
        result: list[str] = []
        if isinstance(rhs, str):
            for item in self.items:
                result.append(item + rhs)
       
        else:
            for i in range(0, len(self.items)):
                result.append(self.items[i] + rhs.items[i])
        return StrArray([result])

        # or
        # if isinstance(rhs, str):
        #     result: StrArray = StrArray([])
        #     for item in self.items:
        #         result.items.append(item + rhs)
        #     return result

    
first: StrArray = StrArray(["Armondo", "Brady", "Caleb"])
last: StrArray = StrArray(["Bacot", "Manek", "Love"])
print(first)
print(first + "!")
print(first)