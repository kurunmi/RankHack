def triplets(nums):
    first = second = float('inf')
    for n in nums:
        if n <= first:
            print("f", n)
            first = n
        elif n <= second:
            print("s", n)
            second = n
        else:
            return True
    return False

if __name__ == '__main__':
    print(triplets([20,100,10,12,5,13]))
