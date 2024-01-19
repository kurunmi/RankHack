#!/usr/bin/python3

def myplace(num):
    position = 0
    index = 0
    count = 0
    index1 = 'x'
    index2 = 'y'
    indic = -1
    flag = False
    mylen = len(num)
    size = mylen - 1
    while position < mylen - 1:
        print("nohit",  index, indic, position, num, index1, index2, count)
        count += 1
        if count > 3 and num[index] == num[index1] and num[index1] == num[index2]:
            size -= 1
            print('hit', index, position, indic, num[index], num[position], num[position + 1], num)
            num[index] = num[position]
            num[position] = ''
            if indic == -1:
                indic = position
            position += 1
            print('hit1', index, position, indic, num[index], num[position], num[position + 1], num)
        else:
            if indic != -1:
                print(num[indic])
                num[indic] = num[position]
                num[position] = ''
                indic += 1
            print('hit4', index, position, indic, num[index], num[position])
            index2 = index1
            index1 = index
            index += 1
            position += 1
            print('hit3', index, position, indic, num[index], num[position])

    return size


if __name__ == '__main__':
    print(myplace([0,0,1,1,1,1,2,3,3]))


