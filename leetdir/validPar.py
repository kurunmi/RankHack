def isValid(s):
    if len(s) % 2 != 0:
        return False
    open_dict = {'(': 'A',
                 '{': 'B',
                 '[': 'C'}

    close_dict = {')': 'A',
                  '}': 'B',
                  ']': 'C'}

    all_vals = {'A': 0,
                'B': 0,
                'C': 0}

    for val in s:
        if val in open_dict:
            all_vals[open_dict[val]] += 1
        else:
            all_vals[close_dict[val]] -= 1
    for attrib in all_vals:
        if all_vals[attrib] != 0:
            return 'false'
    return 'true'


if __name__ == '__main__':
    s = "()"
    s1 = "(]"
    print(isValid(s1))


    