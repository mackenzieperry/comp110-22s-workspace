"""A field of flowers."""

from turtle import Turtle, done
import random

"""For something fun I used turtle.circle() and turtle.dot(). I also used random.choice() to make my flowers random colors."""
"""I also did my best to really break down my functions so no one function got too long or had repeated steps."""

__author__ = "730468950"


def draw_circle(x: int, y: int, size: int, color: str, c_turtle: Turtle) -> None:
    """Draws one circle to make a single petal."""
    c_turtle.color(color)
    c_turtle.penup()
    c_turtle.begin_fill()
    c_turtle.goto(x, y)
    c_turtle.setheading(0.0)
    c_turtle.pendown()
    c_turtle.circle(size)
    c_turtle.end_fill()


def draw_dot(x: int, y: int, turtle: Turtle) -> None:
    """Draws a dot."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("brown")
    turtle.dot(5)


def draw_flower_center(x: int, y: int, turtle: Turtle) -> None:
    """Draws the dots in the middle of the flower."""
    draw_dot(x, y - 5, turtle)
    draw_dot(x, y + 5, turtle)
    draw_dot(x - 5, y, turtle)
    draw_dot(x + 5, y, turtle)


def draw_petals(x: int, y: int, a_turtle: Turtle) -> None:
    """Draws the peals of the flower."""
    color: str = random.choice(["blue", "pink", "purple", "yellow", "red"])
    a_turtle.speed(100)
    draw_circle(x, y, 15, color, a_turtle)
    draw_circle(x - 15, y - 15, 15, color, a_turtle)
    draw_circle(x, y - 30, 15, color, a_turtle)
    draw_circle(x + 15, y - 15, 15, color, a_turtle)
    draw_circle(x, y - 10, 10, "white", a_turtle)
    draw_flower_center(x, y, a_turtle)


def draw_rectangle(x: int, y: int, width: int, lenght: int, b_turtle: Turtle) -> None:
    """Draws a rectange."""
    b_turtle.penup()
    b_turtle.begin_fill()
    b_turtle.goto(x, y)
    b_turtle.setheading(0.0)
    b_turtle.pendown()
    b_turtle.forward(width)
    b_turtle.left(90)
    b_turtle.forward(lenght)
    b_turtle.left(90)
    b_turtle.forward(width)
    b_turtle.left(90)
    b_turtle.forward(lenght)


def draw_stem(x: int, y: int, b_turtle: Turtle) -> None:
    """Draws the stem of a flower."""
    b_turtle.speed(50)
    b_turtle.color("green")
    b_turtle.penup()
    b_turtle.begin_fill()
    b_turtle.goto(x, y)
    draw_rectangle(x, y, 10, 50, b_turtle)
    b_turtle.end_fill()
    stem_outline(x, y, b_turtle)
    draw_square(x - 10, y + 25, "green", b_turtle)


def stem_outline(x: int, y: int, turtle: Turtle) -> None:
    """Draws an outline of the stem in a darker shade of green."""
    turtle.speed(50)
    turtle.color("dark green")
    draw_rectangle(x, y, 10, 50, turtle)


def draw_square(x: int, y: int, color: str, turtle: Turtle) -> None:
    """Draws a square."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.color(color)
    turtle.begin_fill()
    i: int = 0
    while (i < 3):
        turtle.forward(10)
        turtle.left(90)
        i = i + 1
    turtle.end_fill()


def draw_field(x: int, y: int, number_of_flowers: int, turtle1: Turtle, turtle2: Turtle) -> None:
    """Draws the field of flowers."""
    i: int = 0
    while i < number_of_flowers:
        draw_stem(x - 5, y - 70, turtle1)
        draw_petals(x, y, turtle2)
        i += 1
        x += 100


def main() -> None:
    """The entrypoint of my scene."""
    leo: Turtle = Turtle()
    bob: Turtle = Turtle()
    leo.hideturtle()
    bob.hideturtle()
    draw_field(-300, -100, 7, bob, leo)
    draw_field(-450, 0, 9, bob, leo)
    done()


if __name__ == "__main__":
    main()