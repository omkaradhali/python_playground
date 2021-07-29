"""
Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].
"""


def max_sub_array_of_size_k(k, arr):
    s = 0
    temp = 0
    fin = 0

    for i in range(k):
        temp += arr[i]

    s = temp
    for j in range(k, len(arr)):
        s = s - arr[j - k] + arr[j]
        temp = max(temp, s)

    return temp


if __name__ == "__main__":
    print(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2]))
    print(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5]))
