"""
Write a Python program that prints a version of the string s with all commas replaced by dots.
"""


def main(s: str) -> str:
    return s.replace(",", ".")


if __name__ == "__main__":
    print(main("Hello, World!"))
    print(main("3,456,344"))
