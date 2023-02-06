"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

"""
from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    leftmost, rightmost = 1, 1

    left_arr = []
    right_arr = []
    res = []

    left_arr.append(leftmost)
    right_arr.append(rightmost)

    for item in nums:
        val = item*left_arr[len(left_arr) - 1]
        left_arr.append(val)

    for item in range(len(nums), 0, -1):
        val = nums[item-1]*right_arr[0]
        right_arr.insert(0, val)

    left_arr.pop(len(left_arr)-1)
    right_arr.pop(0)

    # print(left_arr)
    # print(right_arr)

    for item in range(len(left_arr)):
        # print(item)
        res.append(left_arr[item] * right_arr[item])

    return res


if __name__ == "__main__":
    print(productExceptSelf([1, 2, 3, 4]))
    print(productExceptSelf([-1, 1, 0, -3, 3]))


# 1 [1, 2, 3, 4] 1

# [1, 1, 2, 6]
# [24, 12, 4, 1]
# 24 12 8 6

# 1 [-1, 1, 0, -3, 3] 1

# [1, -1, -1, 0, 0]
# [0, 0, -9, 3, 1]
# 0, 0, 9, 0, 0
