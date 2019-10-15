import random
import string

# a-z A-Z
str1 = string.ascii_letters
str_num = string.digits
print(str1, str_num)

ran1 = random.random()                   # 随机0,1之间的浮点数
ran2 = random.randint(0, 4)              # 随机区间内的整数
ran3 = random.uniform(0, 4)              # 随机区间内的浮点数
ran4 = random.choice(str1)               # 随机字符串里面的一个字符
ran5 = ''.join(random.sample(str1+str_num, 8))
ran6 = random.choice([1, 2, 3])
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
random.shuffle(items)                   # 打乱排序
print(ran1)
print(ran2)
print(ran3)
print(ran4)
print(ran5)
print(ran6)
print(items)
