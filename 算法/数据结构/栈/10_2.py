from 算法.数据结构.栈.stack import Stack

def change_to_2(num):
    """
    把十进制的数转换为二进制的数
    :param num:
    :return:
    """
    remstack = Stack()
    while num > 0:
        remder = num % 2
        remstack.push(remder)
        num //= 2
    binary_str = ""
    while not remstack.isEmpty():
        binary_str += str(remstack.pop())
    return binary_str


print(change_to_2(20))
