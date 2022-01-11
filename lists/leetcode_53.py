"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Input: nums = [5,4,-1,7,8]
Output: 23
"""


def maxSubArray(nums):
    current_max = 0
    sub_array = []

    if len(nums) == 1:
        return nums[0]

    current_max = nums[0]

    for item in nums:
        if len(sub_array) == 0:
            sub_array.append(item)

        if item > current_max and (sum(sub_array) + item) > current_max:
            current_max = item
            sub_array = [item]

        if item < current_max:
            if current_max < sum(sub_array) + item:
                current_max = sum(sub_array) + item
                sub_array.append(item)
            if current_max > sum(sub_array) + item:
                sub_array = []
                current_max = item
