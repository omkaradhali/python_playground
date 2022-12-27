"""
Write a Python program that check if a string only contains numbers.

If it does, print True. Else, print False.
"""


def main(s: str) -> bool:
    if not len(s):
        return False

    return s.isdigit()


if __name__ == "__main__":
    print(main("Hello"))
    print(main("4567"))
    print(main("Hello59"))
    print(main(""))
