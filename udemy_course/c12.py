"""
Write a Python program that checks if the string s ends with a specific sequence of characters denoted by the variable suffix.

If it does, print True. Else, print False.

This test should be case sensitive. Therefore, "A" should not be equivalent to "a".

If the length of the suffix is greater than the length of the string, print False.
"""


def main(s: str, su: str) -> bool:

    if len(su) > len(s):
        return False
    if s[(len(s) - len(su)):] == su:
        return True

    return False


if __name__ == "__main__":
    print(main("Hello", "ello"))
    print(main("Hello", "Ello"))
    print(main("Coding", "eng"))
    print(main("Nora", "rowing"))
