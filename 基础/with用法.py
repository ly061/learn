#!/usr/bin/env python
# with_example01.py
# 有点类似 try finally的作用， 上下文管理器.进入时调用__enter__,发生异常或者任务结束时自动调用__exit__方法

class Sample:
    def __enter__(self):
        print("In __enter__()")
        return "Foo"

    def __exit__(self, type, value, trace):
        print("In __exit__()")


def get_sample():
    return Sample()


with get_sample() as sample:
    print("sample:", sample)
