"""
Write a Python program that reverses the individual words in the string s and changes their capitalization. Uppercase letters should be printed in lowercase and vice versa.

Assume that the string only contains letters and spaces are used to separate words.
"""


def main(s: str) -> str:
    res = []

    for c in s:
        if not c.isupper():
            res.append(c.upper())
        else:
            res.append(c.lower())
    temp = ''.join(res)


if __name__ == "__main__":
    print(main("Hello World"))
    print(main("Python is Awesome"))
