"""
Input: k = 3, arr = [1, 1, 2, 1, 1]

Output: 2

Explanation: The nice subarrays are [1, 1, 2, 1] and [1, 2, 1, 1].
"""
import copy


def count_nice_subarrays(k, arr):
    # WRITE YOUR BRILLIANT CODE HERE
    left = 0
    result = []
    temp = []
    count = 0
    even_count = 0
    for right in range(len(arr)):
        if count < 3:
            if arr[right] % 2 != 0:
                count += 1
            else:
                even_count += 1
            temp.append(arr[right])
        else:
            temp1 = copy.deepcopy(temp)
            result.append(temp1)
            temp.pop(left)
            temp.append(arr[right])
            left += 1

    if len(temp) and even_count != len(arr):
        result.append(temp)
    print(result)
    return len(result)


if __name__ == "__main__":
    print(count_nice_subarrays(3, [1, 1, 2, 1, 1]))
    print
    print(count_nice_subarrays(1, [2, 4, 6, 8, 10]))
