"""Example of a class and object instantiation."""


class Pizza:
    """Models the idea of a pizza."""

    # Attributes
    size: str = "small"
    toppings: int = 0
    extra_cheese: bool = False

    def __init__(self, size: str, toppings: int) -> None:
        """Creates a pizza."""
        self.size = size
        self.toppings = toppings

    def price(self) -> float:
        """Calculate the price of a pizza."""
        total: float = 0.0
        if self.size == "large":
            total += 10.0
        else:
            total += 8.0
        total += self.toppings * 0.75

        if self.extra_cheese:
            total += 1.0

        return total


a_pizza: Pizza = Pizza('large', 3)
print(Pizza)
print(a_pizza)
print(a_pizza.size)
print(f"Price: ${a_pizza.price()}")

another_pizza: Pizza = Pizza("small", 0)
another_pizza.extra_cheese = True
print(f"Price: ${another_pizza.price()}")