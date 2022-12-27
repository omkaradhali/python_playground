"""
Write a Python program that prints the first and last three characters of the string s as a single string.

If the string has less than six characters, print an empty string (blank output).
"""


def main(s: str) -> str:
    if len(s) < 6:
        return ""

    return s[:3] + s[len(s)-3:]


if __name__ == "__main__":
    print(main("Blue"))
    print(main("Wonderful"))
    print(main("Amazing"))
