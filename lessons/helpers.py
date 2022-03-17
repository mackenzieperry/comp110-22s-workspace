"""Desmonstrates defining a module imported elsewhere."""


def powerful(x: float, n: float) -> float:
    """Raise x to the power of n."""
    return x ** n


def main() -> None:
    print(powerful(2, 10))
    print("helpers.py run as a module")


if __name__ == "__main__":
    main()
else:
    # it is not itomtic to have an else branch here
    print(f"Helpers.py was imported: {__name__}")