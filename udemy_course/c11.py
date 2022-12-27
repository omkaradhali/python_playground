"""
Write a Python program that prints a copy of the string s without any spaces.

Words should be connected in the final string.

If the string doesn't contain spaces, print it intact.
"""


def main(s: str) -> str:
    return s.replace(" ", "")


if __name__ == "__main__":
    print(main("Hello, World!"))
    print(main("Have a great day"))
    print(main("Python"))
