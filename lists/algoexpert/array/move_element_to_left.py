def moveElementToEnd(array, toMove):
    # Write your code here.
    left = 0
    right = left + 1

    while right < len(array):
        if array[left] == toMove:
            if array[right] != toMove:
                array[left], array[right] = array[right],  array[left]
                left += 1
                right += 1
            else:
                right += 1
        else:
            right += 1
            left += 1

    return array


if __name__ == "__main__":
    print(moveElementToEnd([2, 1, 2, 2, 2, 3, 4, 2], 2))
    print(moveElementToEnd([1,2,3,4,5], 3))
