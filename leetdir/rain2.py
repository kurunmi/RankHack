def rain(height):
    left = 0
    right = len(height) -1
    left_max = height[left]
    right_max = height[right]
    total = 0


    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(height[left], left_max)
            total += left_max - height[left]
        else:
            right -= 1
            right_max = max(height[right], right_max)
            total += right_max - height[right]

    return total


if __name__ == '__main__':
    height = [1,2,3,4,5,6]
    height1 = [3,1,3,2,2,3]
    print(rain(height1))