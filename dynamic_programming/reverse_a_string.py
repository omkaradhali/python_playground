"""
Given a string reverse it using D.P
"""

def reverse(s):
    # what is the base case ?
    if (len(s) == 1):
        return s
    
    # What is the least amount f work I can do ?
    return reverse(s[1:]) + s[0]

if __name__ == "__main__":
    print(reverse('hello'))