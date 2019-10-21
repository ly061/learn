# 垃圾回收机制
# 引用计数为主，当引用计数为0时销毁对象
# 标记清除-------解决循环引用，维护引用计数消耗资源
# 分代回收


class Person(object):

    def __del__(self):
        print("销毁对象", id(self))


p1 = Person()
print('p1的id', id(p1))
p2 = Person()
print('p2的id', id(p2))
del p2
print('p2清除完成')

