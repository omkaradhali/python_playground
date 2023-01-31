"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
"""


from collections import Counter
from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
    counter = {}

    for item in nums:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1

    # print(counter)
    counter_sorted = dict(
        sorted(counter.items(), key=lambda x: x[1], reverse=True))

    res = []
    res.extend(list(counter_sorted.keys())[:2])

    return res


def top_k_elements(nums: List[int], k: int) -> List[int]:
    c = Counter(nums)
    nums2 = c.most_common(k)
    print(nums2)
    print(dict(nums2))
    res = []

    for idx in range(len(nums2)):
        res.append(nums2[idx][0])

    print(res)


if __name__ == "__main__":
    print(topKFrequent([1, 1, 1, 2, 2, 3], 2))
    print(topKFrequent([1], 1))

    print(top_k_elements([1, 1, 1, 2, 2, 3], 2))
    print(top_k_elements([1], 1))
