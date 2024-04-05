def canCompleteCircuit(gas, cost):
    if sum(gas) > sum(cost):
        return -1
    cumul = 0
    step = 0
    for index in range(len(gas)):
        cumul += gas[index] - cost[index]
        if cumul < 0:
            step = index + 1
            cumul = 0

    return step
