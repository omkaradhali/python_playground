"""
Given an array of integers, output all the unique pairs that sump to a specific value k

Example:
Input:
pair_sum([1,3,2,2], 4)

Output:
(1,3)
(2,2)
"""

# this code fails for case [1,3,2,2] and 2


def pair_sum(arr, k):
    result = set()
    result_count = 0

    for item in arr:
        if (k - item) in arr:
            result.add((item, (k-item)))
            result_count += 1
            arr.remove(item)

    print(result)
    print()
    print(len(result))


def pair_sum2(arr, k):
    counter = 0
    lookup = set()
    result = []
    for num in arr:
        if k-num in lookup:
            counter += 1
            result.append((num, k-num))
        else:
            lookup.add(num)
    print(lookup)
    print(result)
    return counter



print(pair_sum2([1, 3, 2, 2], 4))
