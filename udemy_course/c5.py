"""
Write a Python program that prints the string s without the characters located at even indices.

If the string is empty or only has one character, print it without any changes.
"""


def main(s: str) -> str:
    if not len(s):
        return ""

    if len(s) == 1:
        return s

    return s[1:len(s):2]


if __name__ == "__main__":
    print(main("Coding"))
    print(main("Pizza"))
    print(main("Python"))
    print(main("A"))
    print(main(""))
