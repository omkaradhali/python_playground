def isMonotonic(array):
    # Write your code here.
    decreasing = False
    increasing = False

    anamoly = False

    if len(array) < 2:
        return True

    first = array[0]
    second = array[1]

    if first >= second:
        decreasing = True

    if first <= second:
        print("Increasing")
        increasing = True

    for index in range(2, len(array)):
        print(index)
        # print(array[index - 1], array[index])
        print(array[index - 1] <= array[index])
        if decreasing and array[index - 1] >= array[index]:

        if increasing and (array[index - 1] <= array[index]):
            print(array[index - 1], array[index])

        else:
            print("ANAMOLY FOUND")
            anamoly = True

    if anamoly:
        return False
    else:
        return decreasing or increasing


if __name__ == "__main__":
    print(isMonotonic([1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 7, 9, 10, 11]))
