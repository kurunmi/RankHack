def isValid(s):
    if len(s) % 2 != 0:
        return False

    open_dict = {'(': 'A',
                 '{': 'B',
                 '[': 'C'}

    close_dict = {')': 'A',
                  '}': 'B',
                  ']': 'C'}

    holder = []

    for item in s:
        if item in open_dict:
            holder.append(item)
        elif not holder or (item != open_dict[holder.pop()]):
            return False
    if holder:
        return False
    return True

if __name__ == '__main__':
    s = "()"
    s1 = "(]"
    print(isValid(s))