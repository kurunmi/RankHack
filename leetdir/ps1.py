def partitionString(s):
    pt = ""
    count = 1
    for i  in s:
        if i in pt:
            pt = ""
            count +=1
        pt += i
    return count


if __name__ == '__main__':
    s = 'abcabbab'
    print(partitionString(s))