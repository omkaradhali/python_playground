import math


def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    first = 0
    second = 0
    m = math.inf
    res = []
    arrayOne.sort()
    arrayTwo.sort()
    while first < len(arrayOne) and second < len(arrayTwo):
        print(first,second)
        s = abs(arrayOne[first] - arrayTwo[second])
        if s < m:
            m = s
            res = [arrayOne[first], arrayTwo[second]]
        if arrayOne[first] < arrayTwo[second]:
            first += 1
        else:
            second += 1
    return res


if __name__ == "__main__":
    r = smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17])
    print(r)
