def calculate(s):
    total, curr_total, sign, stack = 0, 0, 1, []
    for val in s:
        if val.isdigit():
            curr_total = (curr_total * 10) + int(val)
        elif val in '+,-':
            total += curr_total * sign
            curr_total = 0
            if val == '+':
                sign = 1
            else:
                sign = -1
        elif val == '(':
            stack.append(total)
            stack.append(sign)
            total = 0
            sign = 1
        elif val == ')':
            total += sign * curr_total
            total *= stack.pop()
            total += stack.pop()
            curr_total = 0
    return total + (sign * curr_total)






