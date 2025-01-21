def checkpots(flowerpot, n):
    l = len(flowerpot)
    for i in range(l):
        if n <= 0:
            break
        past = flowerpot[i-1] ==0 or i ==0
        fut = i == l -1 or flowerpot[i + 1] == 0
        if flowerpot[i] == 0 and fut and past:
            n -= 1
            flowerpot[i] = 1
    return n <= 0


if __name__ == '__main__':
    print(checkpots([0,0,0,0,0], 3))




