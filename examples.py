from time import sleep
from random import random
from takethetime import ttt


def example_basic():
    with ttt(name="Sleeping is boring, but effective"):
        sleep(0.1)


def example_laps():
    i = 0
    with ttt("You can't fill your lifetime need of sleep in one go") as t:
        for i in range(5):
            sleep(0.02)
            t.lap()


def example_results():
    t = ttt(echo=False)
    with t:
        for i in range(3):
            sleep(0.1 * random())
            t.lap()
    print(t.duration)
    print(t.laps)

if __name__ == "__main__":
    example_basic()
    example_laps()
    example_results()
