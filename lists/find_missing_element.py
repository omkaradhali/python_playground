"""
Consider an array of non negative numbers. A second array is formed
by shuffling the first array and deleting an random number of first array.
Find the missing number in second array.

Example:
Input 
finder([1,2,3,4,5,6,7],[6,7,4,1,3,2])

Output : 5
"""


def finder(arr1, arr2):
    d1 = {}
    for item in arr1:
        if item in d1:
            d1[item] += 1
        else:
            d1[item] = 1

    for item in arr2:
        if item in d1:
            d1[item] -= 1
        else:
            d1[item] = 1

    for items in d1:
        if d1[items] >= 1:
            print(items)


def finder2(arr1, arr2):
    num = 0
    for n in arr1:
        num += n
    for n in arr2:
        num -= n
    return num


def finder3(arr1, arr2):
    arr1.sort()
    arr2.sort()

    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            print(num1)
            return num1

    return arr1[-1]


finder([5,5,7,7], [5,7,7])
