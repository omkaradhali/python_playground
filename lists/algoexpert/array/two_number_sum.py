def twoNumberSum(arr, target):
    lookup = set()

    result = []

    for item in arr:
        if (target - item) in lookup:
            result.append(item)
            result.append(target-item)
        else:
            lookup.add(item)

    return result


if __name__ == "__main__":
    result = twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10)
    print(result)
