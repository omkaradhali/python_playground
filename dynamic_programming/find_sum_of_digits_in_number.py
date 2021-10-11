"""
Given an integer, create a function which returns the sum of all the individual digits in that integer. For example: if n = 4321, return 4+3+2+1
"""

def sum_func(n):
    
    if len(str(n)) == 1:
        return int(n)
    
    return (n%10) + sum_func(n/10)

if __name__ == "__main__":
    print(sum_func(12345))