#!/usr/bin/python3

def newsums(nums):
    trip = []
    pos, neg, zer = [],[], []
    for val in nums:
        if val > 0:
            pos.append(val)
        elif val < 0:
            neg.append(val)
        else:
            zer.append(val)
    sneg = set(neg)
    spos = set(pos)
    if len(zer) >= 3:
        trip.append([0,0,0])
    if zer:
        for val in spos:
            if -1 * val in sneg:
                nval = sorted([val, -1 * val, 0])
                if nval not in trip:
                    trip.append(nval)
    for x in range(len(pos)):
        for y in range(x+1, len(pos)):
            targ = -1 * (pos[x]+ pos[y])
            if targ in sneg:
                tval = sorted([pos[x], pos[y], targ])
                if tval not in trip:
                    trip.append(tval)
    for a in range(len(neg)):
        for b in range(a+1, len(neg)):
            parg = -1 * (neg[a] + neg[b])
            print(parg)
            if parg in spos:
                pval = sorted([neg[a], neg[b], parg])
                if pval not in trip:
                    trip.append(pval)
    return trip




    print(neg, pos, zer)

if __name__ == '__main__':
    arr1 = [-5, -7, 1, 1, 1, 0,0,0,-1, -1, -1, 2]
    arr3 = [0,0,0,0,0,0]
    arr7 = [-1,0,1,2,-1,-4]
    arr2 = [-1,0,1,2,-1,-4]
    arr4 = [-2,-1, -1, 0,1,1,2]
    arr5 = [-4,-2,-2,-2,0,0,0,1,2,2,2,3,3,4,4,6,6]
    print(newsums(arr2))