"""
Implement division of two positive integers without using the division, multiplication, or modulus operators. Return the quotient as an integer, ignoring the remainder.
"""

def division_with_add(num1, num2):
    result = 0
    count = 0
    
    while result < num1:
        result += num2
        count += 1
    
    print(count)

division_with_add(256,2)
    
