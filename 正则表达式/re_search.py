import re


url = 'https://www.baidu.com/en-gb/hongkong/home'

# 匹配语言


def match_lan():
    r = re.search('com/(?P<language>.{5})/', url)
    print(r.group(1))
    print(r.groupdict()['language'])


match_lan()
