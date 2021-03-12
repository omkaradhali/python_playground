"""
Given a string return true if it has unique characters else return false

Input : abcde
Output true

Input : aabcde
output : false
"""

def uni_char1(s):
    seen = []
    
    for item in s:
        if item in seen:
            return False
        else:
            seen.append(item)
    
    return True


def uni_char(s):
    return len(set(s)) == len(s)


print(uni_char("aabcde"))
    

