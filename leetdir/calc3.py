+def calculate(s):
    total, curr_total, sign, stack = 0, 0, 1, []
    for num in s:
        if num.isdigit():
            curr_total = (10 * curr_total) + int(num)
        elif num in '+-':
            total += (sign * curr_total)
            curr_total = 0
            if num == '+':
                sign = 1
            else:
                sign = -1
        elif num == '(':
            stack.append(total)
            stack.append(sign)
            total = 0
            sign = 1
        elif num == ')':
            total += (sign * curr_total)
            total *= stack.pop()
            total += stack.pop()
            curr_total = 0
            sign = 1
    return total + (sign * curr_total)


