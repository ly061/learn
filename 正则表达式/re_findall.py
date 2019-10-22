import re

text = 'https://www.baidu.com/456/123'

r = re.findall('[0-9]{3}', text)
print(r)
