def calculate(s):
    running_total, current_total, sign, stack = 0, 0, 1, []
    for val in s:
        if val.isdigit():
            current_total = (10 * current_total) + int(val)
        elif val in '+-':
            running_total += current_total * sign
            current_total = 0
            if val == '+':
                sign = 1
            else:
                sign = -1
        elif val == '(':
            stack.append(running_total)
            stack.append(sign)
            running_total = 0
            sign = 1
        elif val == ')':
            running_total += current_total * sign
            running_total *= stack.pop() #saved sign
            running_total += stack.pop()
            current_total = 0
    return running_total + (current_total * sign)


