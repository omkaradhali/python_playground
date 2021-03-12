"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""
# Brute force method 
def brute_force(lst, k):
    for i in lst:
        for j in lst:
            if  i != j and i + j == k:
                return True


# using Set O(n) as lookup in sets take O(1)
def first_method(lst, k):
    seen = set()  
    for item in lst:
        if k - item in seen:
            return True
        seen.add(item)


# Second method using binary tree logic. 
from bisect import bisect_left

def second_method(lst, K):
    lst.sort()

    for i in range(len(lst)):
        target = K - lst[i]
        j = binary_search(lst, target)

        # Check that binary search found the target and that it's not in the same index
        # as i. If it is in the same index, we can check lst[i + 1] and lst[i - 1] to see
        #  if there's another number that's the same value as lst[i].
        if j == -1:
            continue
        elif j != i:
            return True
        elif j + 1 < len(lst) and lst[j + 1] == target:
            return True
        elif j - 1 >= 0 and lst[j - 1] == target:
            return True
    return False

def binary_search(lst, target):
    lo = 0
    hi = len(lst)
    ind = bisect_left(lst, target, lo, hi)

    if 0 <= ind < hi and lst[ind] == target:
        return ind
    return -1


if __name__ == "__main__":
    lst = [10, 15,3,7]
    k = 17
    print(brute_force(lst, k))
    print(first_method(lst, k))
    print(second_method(lst, k))