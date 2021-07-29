"""
Given a Decimal number convert to binary
"""

def helper(num, res):
    
    # What is the base case
    if num == 0:
        return res
    
    # What is the smallest amount of work I can do in each iteration.
    res  = str(num % 2) + res
    return helper(num//2, res)

def decimal_to_binary(num):
    res = ""
    return helper(num,res)


if __name__ == "__main__":
    print(decimal_to_binary(233))