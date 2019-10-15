# 列表推导式
li1 = [x for x in range(5)]
li2 = [[x for x in range(3)] for x in range(3)]
li3 = [[x for x in range(3)] for x in range(3) if x > 0]
li4 = [(x, y) for x in range(3) for y in range(3)]
print(li1, li2, li3, li4, sep='\n')

# 字典推导式
text = 'i love you'
dic1 = {x: text.count(x) for x in text}
print(dic1)

# 生成器推导式（元祖推导式）
# 一个生成器只能运行一次，第一次迭代可以得到数据，第二次迭代就是空
gen = (x for x in range(10))
for i in gen:
    print(i, end='')
for j in gen:
    print(j)
    print('--------------')


