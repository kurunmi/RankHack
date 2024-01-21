#!/usr/bin/python3
import math

def arrayprod(nums):
    prods = [1] * len(nums)
    prod1 = []
    right_prod = 1
    for r in range(len(nums)-1, -1, -1):
        right_prod *= nums[r]
        prods[r] = right_prod
    left_prod = 1
    old_val = 1
    for index in range(len(nums)):
        val = prods[index+1] if (index < len(nums) - 1) else 1
        left = nums[:index]
        prods[index] = left_prod * val
        left_prod *= nums[index]
        old_val = val
    #prods.pop()
    #prods.append(left_prod)
    return(prods)



if __name__ == '__main__':
    print(arrayprod([2,3,4,5,6]))