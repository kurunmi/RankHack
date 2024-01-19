#!/usr/bin/python3

def candy(ratings):
    deltas = 0
    total = len(ratings)
    increment = 0
    last_act = False
    act = None
    last_max = 0
    prev = ratings[0]
    for i in range(len(ratings)):
        val = ratings[i]
        inc = 0
        if val == prev:
            act = 'flat'
            increment = 0
            #if last_act == 'flat':
        if val > prev:
            act = 'incr'
            if last_act == 'decr':
                increment = 0
                increment += 1
                deltas += increment
            if last_act == 'incr':
                increment += 1
                deltas += increment
            if last_act == 'flat':
                increment = 0
                increment += 1
                deltas += increment
        if val < prev:
            act = 'decr'
            if last_act == 'decr':
                increment += 1
                deltas += increment
            if last_act == 'flat':
                increment = 0
                increment += 1
                deltas += increment
            if last_act == 'incr':
                increment = 0
                increment += 1
        print(val, prev, act, last_act, increment, deltas)
        prev = val
        prev_act = last_act
        last_act = act

    return deltas + total


if __name__ == '__main__':
    print(candy([1,6,10,8,7,3,2]))

1,3,2,2,1

1,3,4,5,2

#1,6,10,8,7,3,2 18

#1,2,3,1,0 9

#29,51,87,87,72,12 12
#[1,2,87,87,87,2,1] 13

[1,2,3,1,0]
