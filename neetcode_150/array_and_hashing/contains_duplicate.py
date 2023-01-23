"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""


from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    print(len(set(nums)) != len(nums))


if __name__ == "__main__":
    contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
    contains_duplicate([1, 2, 3, 4])
    contains_duplicate([1, 2, 3, 1])
