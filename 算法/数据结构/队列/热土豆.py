from 算法.数据结构.队列.queue import Queue


def hot_potato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)
    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
        simqueue.dequeue()
    print(simqueue)
    return simqueue.dequeue()

print(hot_potato(["01", "02", "03", "04", "05", "06", "07"], 3))