with open('./文件操作/README', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    lines = [str(index)+' '+line for index, line in enumerate(lines)]

with open('./文件操作/README', 'w', encoding='utf-8') as f:
    f.writelines(lines)


