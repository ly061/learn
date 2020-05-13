import threading
import requests


class myThread(threading.Thread):
    def __init__(self, threadID, name, s, e):
        super().__init__()
        self.threadID = threadID
        self.name = name
        self.s = s
        self.e = e

    def run(self):
        print("start")
        threadLock.acquire()
        # 线程需要执行的方法
        test_url(self.s, self.e)
        # 释放锁
        threadLock.release()


def read_data():
    with open('test.txt') as f:
        data = f.readlines()
    return data

def test_url(s,e):
    for i in range(s, e):
        re = requests.get(read_data()[i].replace("\n", ""))
        print(re.status_code, read_data()[i])
        if re.status_code != 200:
            print(re.status_code, read_data()[i])

if __name__ == '__main__':
    totalThread = 10  # 需要创建的线程数，可以控制线程的数量
    lenList = len(read_data())  # 列表的总长度
    gap = int(lenList / totalThread)  # 列表分配到每个线程的执行数
    threadLock = threading.Lock()  # 锁
    threads = []  # 创建线程列表
    for i in range(totalThread):
        thread = 'thread%s' % i
        if i == 0:
            thread = myThread(0, "Thread-%s" % i, 0, gap)
        elif totalThread == i + 1:
            thread = myThread(i, "Thread-%s" % i, i * gap, lenList)
        else:
            thread = myThread(i, "Thread-%s" % i, i * gap, (i + 1) * gap)
        threads.append(thread)  # 添加线程到列表
    for i in range(totalThread):
        threads[i].start()
