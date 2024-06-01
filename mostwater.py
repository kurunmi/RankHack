def maxArea(height):

    start = 0
    end = len(height) -1
    area = 0

    while start < end:
        area = max(area, min(height[start],  height[end]) * (end - start))

        if height[end] < height[start]:
            end -= 1
        else:
            start += 1
    return area


if __name__ == '__main__':
    height = [1,8,6,2,5,4,8,3,7]
    height1 = [1,1]
    print(maxArea(height1))