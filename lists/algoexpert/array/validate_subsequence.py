def isValidSubsequence_not_working(array, sequence):
    seq = 0
    result = False

    for item in array:
        if item in sequence and sequence.index(item) >= seq:
            seq = sequence.index(item)
            result = True
        else:
            result = False

    return result


def isValidSubsequence(array, sequence):
    # Write your code here.
    seq_pointer = 0
    print(sequence)
    for item in array:
        if seq_pointer < len(sequence):
            if sequence[seq_pointer] == item:
                seq_pointer += 1
            else:
                continue
    if seq_pointer == len(sequence):
        return True
    return False


if __name__ == "__main__":
    result = isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10])
    print(result)
