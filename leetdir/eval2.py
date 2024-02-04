def evalRPN(tokens):
    stack = []
    ops = {'+', '-', '/', '*'}
    for item in tokens:
        if item in ops:
            a, b = stack.pop(), stack.pop()
            if item == '+':
                stack.append(a + b)
            elif item == '-':
                stack.append(b -a)
            elif item == '*':
                stack.append( b * a)
            elif item == '/':
                stack.append(int(float(b / a)))
        else:
            stack.append(int(item))
    return stack[0]

if __name__ == '__main__':
    tokens = ["2", "1", "+", "3", "*"]
    tokens2 = ["4", "13", "5", "/", "+"]
    tokens1 =  ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(evalRPN(tokens2))
