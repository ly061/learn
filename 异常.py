def input_pwd():
    pwd = input('请输入密码:')
    if len(pwd) >= 8:
        return pwd
    raise Exception('密码长度不够')

try:
    print(input_pwd())
except Exception as err:
    print(err)
