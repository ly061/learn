import re
with open('../test111') as f:
    test_text = f.read()

# pattern = re.compile(r'/\s.{17}0.9')
# res = pattern.findall(test_text)
# time_replace = 0
# for i in res:
#     time_replace += 1
#     test_text = test_text.replace(i+' ', '\n')
#
# with open(r'../test2222', 'w') as f:
#     f.write(f'There are {time_replace} urls in this file\n')
#     f.writelines(test_text)

r = re.sub(r'/\s.{17}0.9 ?', '\n', test_text)

with open(r'../test2222', 'w') as f:
    f.write(f'There are  urls in this file\n')
    f.write(r)
