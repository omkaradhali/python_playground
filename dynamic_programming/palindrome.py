"""
Given a string determine if its a plaindrome.
"""

def is_palindrome(s):
    # What is the base case
    if len(s) == 0 or len(s) == 1:
        return True
    
    # What is the smallest amount of work I can do in each iteration
    if s[0] == s[len(s) - 1]:
        return is_palindrome(s[1:len(s)-1])
    
    return False


if __name__ == "__main__":
    print(is_palindrome('kayak'))