import pytest
import random


@pytest.mark.run(order=11)
def test1():
    s = 0
    for i in range(100000000):
        s += i
    return s



@pytest.mark.run(order=1)
def test2():
    s = 0
    for i in range(100000000):
        s += i
    return s

@pytest.mark.run(order=3)
def test3():
    s = 0
    for i in range(100000000):
        s += i
    return s


@pytest.mark.flaky(reruns=6, reruns_delay=2)
def test4():
    s = 0
    for i in range(100000000):
        s += i
    return s

