"""
Write a Python Program that prints the reversed version of a string.

The program must preserve uppercase and lowercase letters.

If the string is empty, print it intact.
"""


def main(s: str) -> str:
    if not len(s):
        return ""

    res = ""
    for item in range(len(s)-1, -1, -1):
        res += s[item]
        if item == 0:
            return res


if __name__ == "__main__":
    print(main("Hello"))
    print(main("Wo"))
    print(main(""))
