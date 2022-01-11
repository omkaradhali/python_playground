def sortedSquaredArray_not_working(array):
    left = 0
    right = len(array) - 1
    result = []

    while left <= right:
        square_left = array[left] * array[left]
        square_right = array[right] * array[right]

        if square_left > square_right:
            array[right], array[left] = array[left], array[right]

            left += 1
        else:
            right -= 1
    # print(array)
    for item in array:
        result.append(item*item)
    return result


def sortedSquaredArray(array):
    # Write your code here.
    left = 0
    right = len(array) - 1
    result = [0 for _ in array]

    for i in reversed(range(len(array))):
        leftval = array[left]
        rightval = array[right]

        if abs(leftval) > abs(rightval):
            result[i] = leftval * leftval
            left += 1
        else:
            result[i] = rightval * rightval
            right -= 1

    return result


if __name__ == "__main__":
    result = sortedSquaredArray([-2, 1, 3, 4, 5, 6])
    res2 = sortedSquaredArray([-10, -5, 0, 5, 10])
    res3 = sortedSquaredArray([-5, -4, -3, -2, -1])
    print(result)
    print(res2)
    print(res3)
