import re

text = 'https://www.baidu.com/456/123'

r = re.search('([0-9]{3})/([0-9]+)', text)
print(r.group())
print()
print(r.group(1))
print(r.group(2))

