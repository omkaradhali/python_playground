def main():
    f = open('input.txt')

    clean_data = list(map(lambda data: int(data.strip()), f.readlines()))

    left = 0
    right = 3

    previous_sum = 0

    result = []

    while right <= len(clean_data):
        temp = sum(clean_data[left:right])
        if temp > previous_sum:
            if left != 0:
                result.append("i")
        previous_sum = temp
        left += 1
        right += 1

    return len(result)


if __name__ == "__main__":
    print(main())