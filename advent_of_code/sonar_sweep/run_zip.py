def main():
    f = open("input.txt")

    clean_data = list(map(lambda data: int(data.strip()), f.readlines()))
    result = []

    for prev_, next_ in zip(clean_data[:-1], clean_data[1:]):
        if next_ > prev_:
            result.append('i')

    return len(result)


if __name__ == "__main__":
    print(main())
