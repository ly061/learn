import pytest
import time


@pytest.mark.run(order=11)
def test1():
    time.sleep(2)
    s = 0
    for i in range(100000000):
        s += i
    return s



@pytest.mark.run(order=1)
def test2():
    time.sleep(2)
    s = 0
    for i in range(100000000):
        s += i
    return s

@pytest.mark.run(order=3)
def test3():
    time.sleep(2)
    s = 0
    for i in range(100000000):
        s += i
    return s


@pytest.mark.flaky(reruns=6, reruns_delay=2)
def test4():
    time.sleep(2)
    s = 0
    for i in range(100000000):
        s += i
    return s

