"""
Write a Python program that prints the string s without the character at index n.

If the index n is out of range, print the string s intact.

If the string s is empty, print the string s intact.
"""


def main(s: str, index: int) -> str:

    if len(s) < index:
        return s

    res = ""
    for i in range(len(s)):
        if i == index:
            continue
        res += s[i]

    return res


if __name__ == "__main__":
    print(main("Hello", 1))
    print(main("World", 3))
    print(main("Dog", 15))
    print(main("", 2))
