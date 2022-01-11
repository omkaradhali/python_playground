def threeNumberSum(array, targetSum):
    # Write your code here.
    result = []
    array.sort()

    for i in range(len(array)):
        left = i + 1
        right = len(array) - 1
        remainder = targetSum - array[i]
        while left < right:
            add = array[left] + array[right]
            if add == remainder:
                result.append([array[i], array[left], array[right]])
                left = left + 1
            elif add < remainder:
                left = left + 1
            elif add > remainder:
                right = right - 1

    print(result)


if __name__ == "__main__":
    threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0)
