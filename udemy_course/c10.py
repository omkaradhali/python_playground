"""
Write a Python program that checks if the string s contains all the letters in the alphabet (case-insensitive, so "A" should be equivalent to "a").

If it does, print True. Else, print False.

Before comparing the characters, you should convert the string to lowercase.

If the string contains spaces, ignore them before finding the result.

You may assume that the string doesn't contain any other symbols, only spaces (possibly).

Consider these letters as part of the alphabet: 'abcdefghijklmnopqrstuvwxyz'
"""

import string


def main(s: str) -> bool:
    a = "abcdefghijklmnopqrstuvwxyz"

    for char in a:
        if char in s.lower():
            continue
        else:
            return False

    return True


if __name__ == "__main__":
    print(main("abcdefghijklmnopqrstuvwxyz"))
    print(main("The quick brown fox jumps over the lazy dog"))
    print(main("Hello"))
