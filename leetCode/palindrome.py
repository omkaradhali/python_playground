def isPalindrome(a):
    """
    :type s: str
    :rtype: bool
    """
    s = ""

    for item in a:
        print(s)
        if item.isalpha():
            s += item.lower()
        else:
            continue

    print(s)
    if len(s) > 0:
        left = 0
        right = len(s) - 1

        while left < right:
            print(s[left], s[right])
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
    return True


if __name__ == "__main__":
    print("something")
    print(isPalindrome("race a car"))
