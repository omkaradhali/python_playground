def test1(val):
    if val:
        return val
    else:
        return None


def test2(val):
    if val:
        return val
    else:
        return


def test3(val):
    if val:
        return val


if __name__ == "__main__":
    print(test1(0))
    print(test2(0))
    print(test3(0))

# output
# None
# None
# None
