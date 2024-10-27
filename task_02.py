import turtle
import math


def draw_pythagoras_tree(t, length, level):
    if level == 0:
        t.forward(length)
        t.backward(length)
    else:
        t.forward(length)
        t.left(45)

        draw_pythagoras_tree(t, length * math.sqrt(2) / 2, level - 1)

        t.right(90)

        draw_pythagoras_tree(t, length * math.sqrt(2) / 2, level - 1)

        t.left(45)
        t.backward(length)


if __name__ == "__main__":
    level = int(input("Введіть рівень рекурсії (рекомендується 5-8): "))
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.title("Pythagoras Tree Fractal")

    t = turtle.Turtle()
    t.speed(0)
    t.left(90)

    draw_pythagoras_tree(t, 100, level)

    screen.exitonclick()
