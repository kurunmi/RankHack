#!/usr/bin/python3

def looper(gas, cost):
    step = 0
    residual = 0
    current = 0
    for r in range(len(gas)):
        current += gas[r] - cost[r]
        if current < 0:
            residual += current
            current = 0
            step += 1
    if current + residual >= 0:
        return step
    return -1





if __name__ == '__main__':
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    print("loop", looper(gas, cost))


