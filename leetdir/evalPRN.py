import operator
def evalRPN(tokens):
    stack = []
    operators = {  '+': operator.add,
                    '-': operator.sub,
                    '*': operator.mul,
                    '/': operator.truediv
                    }
    for item in tokens:
        if item not in operators:
            stack.append(int(item))
        else:
            print(stack[-1], stack[-2], item)
            num1 = stack.pop()
            num2 = stack.pop()
            result = int(operators[item](num2, num1))
            print(result)
            if item == '/' and -1 < result < 1:
                stack.append(0)
            else:
                stack.append(result)
    return stack[0]


if __name__ == '__main__':
    tokens = ["2", "1", "+", "3", "*"]
    tokens2 = ["4", "13", "5", "/", "+"]
    tokens1 =  ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(evalRPN(tokens1))