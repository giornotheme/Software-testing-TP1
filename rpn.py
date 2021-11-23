import operator


def rpn(stringtotest):
    ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    splitstring = stringtotest.rsplit(' ')
    stack = []
    i = 0
    while i < len(splitstring):
        if splitstring[i] not in ops:
            splitstring[i] = int(splitstring[i])
            stack.append(int(splitstring[i]))
            print(stack)
            i = i + 1
        elif splitstring[i] in ops:
            if splitstring[i] == "+":
                temp = splitstring[0] + splitstring[1]
                stack.clear()
                stack.append(temp)
                print(stack)
                i = i + 1
            elif splitstring[i] == "-":
                temp = stack[0] - stack[1]
                stack.clear()
                stack.append(temp)
                print(stack)
                i = i + 1
            elif splitstring[i] == "*":
                temp = stack[0] * stack[1]
                stack.clear()
                stack.append(temp)
                print(stack)
                i = i + 1
    return stack[0]
