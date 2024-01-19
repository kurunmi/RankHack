#!/usr/bin/python3

def flytrap(height):
    left_bucket = 0
    right_bucket = 0
    left_bucket_start = False
    right_bucket_start = False
    current = False
    previous = False
    bigbucket = 0
    x = len(height)
    #print(len(height))
    i = 0
    while i < x:
        #y = x - (i + 1)
        val = height[i]
        #right_val = height[y]
        #print(val, right_val, i, y)
        #if i < y + 1:
        if left_bucket_start is False:
            left_bucket_start = i
        if val >= height[left_bucket_start]:
            bigbucket += left_bucket
            left_bucket = 0
            left_bucket_start = i
        if val < height[left_bucket_start]:
            left_bucket += (height[left_bucket_start] - val)
        i += 1
    newheight = (height[left_bucket_start:x])
    newmax = newheight[-1]
    new_bucket_start = False
    y = len(newheight) -1
    inbucket = 0
    while y >= 0:
        if new_bucket_start is False:
            new_bucket_start = newheight[0]
        newval = newheight[y]
        if newval >= newmax:
            newmax = newval
            new_bucket_start = y
        if newval < newmax:
            inbucket += (newmax - newval)
        y -= 1
    return bigbucket + inbucket

if __name__ == '__main__':
    print(flytrap([0,1,0,2,1,0,1,3,2,1,2,1]))


#4,2,0,3,2,5 9
#0,1,0,2,1,0,1,3,2,1,2,1 6
#6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3 83