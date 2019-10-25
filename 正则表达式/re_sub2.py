import re


# 将匹配的数字乘以 2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)


s = 'A23G4HFD567'
# print(re.sub('(?P<value>\d+)', double, s))
r = re.search('(?P<value1>\d+)\w(?P<value2>\d+)', s)
print(r.group())
print(r.groupdict())
print(r.groupdict()['value1'])
print(r.groupdict()['value2'])
# print(r.group(1))
# print(r.group('value'))

