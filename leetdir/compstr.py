def compress(chars):
    current = ""
    count = 0
    loc = 0
    for c in chars:
        if c != current:
            if count > 1:
                for n in str(count):
                    chars[loc] = n
                    loc += 1
            chars[loc] = c
            loc += 1
            count = 1
            current = c
        else:
            count += 1
    if count > 1:
        for n in str(count):
            chars[loc] = n
            loc += 1
        print(chars)
    chars = chars[:loc]
    print(chars)
    return loc



if __name__ == '__main__':
    print(compress(['a','a','b','b', 'c', 'c', 'c']))
