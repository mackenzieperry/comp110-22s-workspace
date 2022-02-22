"""Demonstrates asking the user for input"""

user_name: str = input("What is your name? ")

print("Hello, " + user_name + ", good morning!")
print("You are awesome, " + user_name)

x: int = 0

def f() -> None:
  x: int = 1

f()
print(x)