from turtle import *
import math


def hearta(k):
    return 16 * math.sin(k) ** 3


def heartb(k):
    return 13 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)


def draw_heart():
    speed(0)
    bgcolor("black")

    setup(width=800, height=800)

    penup()
    goto(0, -300)
    pendown()

    color("#f73487")
    hideturtle()

    tracer(0)

    for i in range(3600):
        goto(hearta(i) * 10, heartb(i) * 10)
        dot(5)
        update()

    done()


if __name__ == "__main__":
    draw_heart()
