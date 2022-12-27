"""
Write a Python program that prints the string s with the character curr_char replaced by the character new_char.

curr_char and new_char are variables that contain strings with a single character.

You may assume that new_char will not be an empty string.

The match must be case-sensitive (do not replace lowercase letters if curr_char is uppercase).

If no match is found, print the initial string.
"""


def main(s: str, curr_char: str, new_char: str) -> str:
    return s.replace(curr_char, new_char)


if __name__ == "__main__":
    print(main("Hello", "l", "s"))
    print(main("World", "W", "A"))
    print(main("Python", "P", "x"))
    print(main("Python", "p", "a"))
