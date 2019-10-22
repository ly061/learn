import re

phone = "2004-959-559 # 这是一个国外电话号码"

# 删除字符串中的 Python注释
r1 = re.sub("#.*", '', phone)
print(r1)

# 删除字符串中的-
r2 = re.sub('-*', '', r1)
print(r2)
