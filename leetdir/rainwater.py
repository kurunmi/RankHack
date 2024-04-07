def rain(height):
    current = []
    total = 0
    last_max = False
    current_max = 0
    prev = 0
    for i in height:
        if i > current_max:
            current_max = i
            print(current_max, current, total)
        elif i < current_max:
            tmp_max = min(current_max, last_max) if last_max else current_max
            last_max = current_max
            current_max = 0
            while current:
                total += tmp_max - current.pop()
        current.append(i)
    tmp_max = min(current_max, last_max) if last_max else current_max
    while current:
        total += tmp_max - current.pop()
    return total





if __name__ == '__main__':
    height = [1,2,3,4,5,6]
    height1 = [3,1,3,2,2,3]
    print(rain(height1))



