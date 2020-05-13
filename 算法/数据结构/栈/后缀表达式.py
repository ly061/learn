from 算法.数据结构.栈.stack import Stack


def postfix(infix):
    """
    把中缀表达式变为后缀表达式
    A + B * C变为
    ABC*+
    :param prefix:
    :return:
    """
    # 首先定义操作符的优先级存在字典中
    priority = {}
    priority["*"] = 3
    priority["/"] = 3
    priority["+"] = 2
    priority["-"] = 2
    priority["("] = 1
    stack = Stack()
    postfix_list = []
    # 把表达式分割
    tokenlist = infix.split()
    for token in tokenlist:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfix_list.append(token)
        elif token == "(":
            stack.push(token)
        elif token == ")":
            top_token = stack.pop()
            while top_token != "(":
                postfix_list.append(top_token)
                top_token = stack.pop()
        else:
            while (not stack.isEmpty()) and (priority[token] < priority[stack.peek()]):
                postfix_list.append(stack.pop())
            stack.push(token)
    while not stack.isEmpty():
        postfix_list.append(stack.pop())
    postfix_str = "".join(postfix_list)
    print(postfix_str)
    return postfix_str


def do_math(opration, op1, op2):
    return eval(op1+opration+op2)


def get_value_postfix(infix):
    postfix_li = list(postfix(infix))
    stack = Stack()
    for index in postfix_li:
        if index in "0123456789":
            stack.push(index)
        else:
            op2 = str(stack.pop())
            op1 = str(stack.pop())

            stack.push(do_math(index,op1,op2))
    print(stack.size(), stack.peek())


get_value_postfix("1 + 2 * 3")
