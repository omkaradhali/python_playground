def strStr(haystack: str, needle: str) -> int:
    if needle not in haystack:
        return -1

    needle_length = len(needle)

    for x in range(len(haystack) - needle_length + 1):
        print(x, x+needle_length)
        temp = haystack[x:x+needle_length]
        print(temp)
        if temp == needle:
            return x


if __name__ == "__main__":
    print(strStr("heell", "ll"))
