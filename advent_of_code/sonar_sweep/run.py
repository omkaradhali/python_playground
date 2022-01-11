def main():
    f = open("input.txt")

    data = f.readlines()
    result = []

    for index, item in enumerate(data):
        if index == 0:
            continue

        if int(item.strip()) > int(data[index - 1].strip()):
            result.append('i')
        else:
            continue

    return len(result)


if __name__ == "__main__":
    print(main())
