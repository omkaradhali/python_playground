"""
Write a Python program that prints the character at index i in the string s.

If the index is out of range, the program should print "i is out of range"

If the string is empty, the program should print "Empty String"
"""


def main(s: str, index: int) -> str:

    if not len(s):
        return "Empty String"

    if len(s) >= index-1:
        return s[index]
    else:
        return "i is out of range"


if __name__ == "__main__":
    print(main("Hello", 2))
    print(main("Pizza", 4))
    print(main("", 3))
    print(main("World", 15))
