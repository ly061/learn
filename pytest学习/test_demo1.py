import pytest
import time

@pytest.mark.ly
@pytest.mark.run(order=11)
def test1():
    print('test1 begin')
    # time.sleep(2)
    s = 0
    for i in range(100000000):
        s += i
    return s



@pytest.mark.run(order=1)
def test2():
    print('test2 begin')
    # time.sleep(2)
    s = 0
    for i in range(100000000):
        s += i
    print('test2 end')
    return s

@pytest.mark.run(order=3)
def test3():
    print('test3 begin')
    # time.sleep(2)
    s = 0
    for i in range(100000000):
        s += i
    return s


@pytest.mark.flaky(reruns=6, reruns_delay=2)
def test4():
    print('test4 begin')
    # time.sleep(2)
    s = 0
    for i in range(100000000):
        s += i
    return s

