"""
Reverse a given string. Do not slice (e.g. string[::-1]) or use iteration, there must be a recursive call for the function.
"""

def solution(s):
    
    if (len(s) == 1):
        return s
    
    return s[len(s) - 1] + solution(s[0:len(s) - 1])

if __name__ == "__main__":
    print(solution("hello world"))
    print(solution('123456789'))


