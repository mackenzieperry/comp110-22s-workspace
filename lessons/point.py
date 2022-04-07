from __future__ import annotations


class Point: 
    x: float
    y: float

    def __init__(self, x: float, y: float) -> None:
        """Construct a point giving x and y."""
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        """Special request to represent object as string."""
        return f"{self.x}, {self.y}"

    def __mul__(self, factor: float) -> Point:
        """Overload the mulitiplication operator form Point * float"""
        return Point(self.x * factor, self.y * factor)

    def scale(self, factor: float) -> Point:
        """Scale a point's attributes by factor."""
        # x: float = self.x * factor
        # y: float = self.y * factor
        # p: Point = Point(x, y)
        return Point(self.x * factor, self.y * factor)
    
    def __add__(self, rhs: Point) -> Point:
        print("add was called")
        return Point(self.x + rhs.x, self.y + rhs.y)

    def __gititem__(self, index: int) -> float:
        if index == 0:
            return self.x
        if index == 1:
            return self.y
        else:
            raise IndexError


a: Point = Point(1.0, 2.0)
b: Point = a * 2.0
c: Point = a + b
print(f"b {b}")
print(f"c: {c}")
