"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
"""

from typing import List
from collections import Counter


def top_k_elements(nums: List[int], k: int) -> List[int]:
    c = Counter(nums)
    nums2 = c.most_common(k)
    print(nums2)
    print(dict(nums2))
    res = []

    for idx in range(len(nums2)):
        res.append(nums2[idx][0])

    print(res)


top_k_elements([1, 1, 1, 2, 2, 3], 2)
