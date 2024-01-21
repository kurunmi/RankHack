#!/usr/bin/python3

y
def plusMinus(arr):
    pos = 0
    neg = 0
    zer = 0
    count = 0
    for rec in arr:
        count += 1
        if rec > 0:
            pos += 1
        elif rec < 0:
            neg += 1
        elif rec == 0:
            zer += 1
    pos_ratio = pos / count
    neg_ratio = neg / count
    zer_ratio = zer / count
    print("%6f" % pos_ratio)
    print("%f" % neg_ratio)
    print("%f" % zer_ratio)






if __name__ == '__main__':
    myarr = [1,1,0,-1,-1]
    plusMinus(myarr)